import os
import re
import pytest
from cookiecutter.exceptions import FailedHookException
from binaryornot.check import is_binary
from contextlib import contextmanager
import subprocess
import shlex

PATTERN = r"{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)


@pytest.fixture
def context():
    return {
        "project_name": "Masonite Test Package",
        "project_slug": "masonite-test-package",
        "pkg_name": "test_package",
        "project_description": "A short description of the project.",
        "full_name": "Test Author",
        "email": "test@example.com",
        "github_username": "testauthor",
        "pypi_username": "testauthor",
        "version": "0.0.1",
        "repository": "https://github.com/testauthor/masonite-test-package",
        "python_min": "3.6",
    }


SUPPORTED_COMBINATIONS = [
    {"open_source_license": "MIT"},
    {"open_source_license": "BSD"},
    {"open_source_license": "ISC"},
    {"open_source_license": "GNU General Public License v3"},
    {"open_source_license": "Apache Software License 2.0"},
    {"open_source_license": "Not open source"},
]


def _fixture_id(ctx):
    """Helper to get a user friendly test name from the parametrized context."""
    return "-".join(f"{key}:{value}" for key, value in ctx.items())


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    """Method to check all paths have correct substitutions."""
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue

        for line in open(path, "r"):
            match = RE_OBJ.search(line)
            assert match is None, f"cookiecutter variable not replaced in {path}"


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


@pytest.mark.parametrize("slug", ["masonite-package", "masonite-super-package"])
def test_project_slug_are_valid(cookies, context, slug):
    """Check list contains valid pip package names"""
    context.update({"project_slug": slug})
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0


@pytest.mark.parametrize("slug", ["project slug", "proJect", "Project Slug"])
def test_invalid_project_slug_if_no_pip_installable(cookies, context, slug):
    """Invalid slug should failed pre-generation hook."""
    context.update({"project_slug": slug})
    result = cookies.bake(extra_context=context)
    assert result.exit_code != 0
    assert isinstance(result.exception, FailedHookException)


@pytest.mark.parametrize(
    "slug", ["project-slug", "project", "project_slug", "project-masonite"]
)
def test_invalid_project_slug_if_no_masonite_namespace(cookies, context, slug):
    """Invalid slug should failed pre-generation hook."""
    context.update({"project_slug": slug})
    result = cookies.bake(extra_context=context)
    assert result.exit_code != 0
    assert isinstance(result.exception, FailedHookException)


@pytest.mark.parametrize("pkg", ["package", "super_package", "settings_12"])
def test_package_names_are_valid(cookies, context, pkg):
    """Check list contains valid Python package names"""
    context.update({"pkg_name": pkg})
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0


@pytest.mark.parametrize(
    "pkg", ["project slug", "Project_Slug", "project-slug", "project.slug"]
)
def test_invalid_package_name_if_not_python_importable(cookies, context, pkg):
    """Invalid package should failed pre-generation hook."""
    context.update({"pkg_name": pkg})
    result = cookies.bake(extra_context=context)
    assert result.exit_code != 0
    assert isinstance(result.exception, FailedHookException)


@pytest.mark.parametrize(
    "pkg", ["masonite_project", "masoniteproject", "package_masonite"]
)
def test_invalid_package_name_if_contains_masonite(cookies, context, pkg):
    """Invalid package should failed pre-generation hook."""
    context.update({"pkg_name": pkg})
    result = cookies.bake(extra_context=context)
    assert result.exit_code != 0
    assert isinstance(result.exception, FailedHookException)


@pytest.mark.parametrize("context_override", SUPPORTED_COMBINATIONS, ids=_fixture_id)
def test_project_generation(cookies, context, context_override):
    """Test that project is generated and fully rendered."""

    result = cookies.bake(extra_context={**context, **context_override})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["project_slug"]
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)


def test_generation_and_run_tests(cookies, context):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.project.isdir()
    run_inside_dir("cp .env-example .env", str(result.project)) == 0
    run_inside_dir("pip install -r requirements.txt", str(result.project)) == 0
    run_inside_dir("pip install .", str(result.project)) == 0
    run_inside_dir("python -m pytest tests", str(result.project)) == 0


def test_flake8_passes(cookies, context):
    """Generated project should pass flake8,
    for now only packages sources (src/*)"""
    result = cookies.bake(extra_context=context)
    run_inside_dir("make lint", str(result.project))


def test_black_passes(cookies, context):
    """Generated project should pass black,
    for now only packages sources (src/*)"""
    result = cookies.bake(extra_context=context)
    run_inside_dir("make format", str(result.project))


@pytest.mark.skipif(True, reason="to be debugged")
def test_can_install_package_with_craft(cookies, context):
    """Generated project should pass black,
    for now only packages sources (src/*)"""
    # TODO: make this test pass, I don't understand why the package can't be installed
    result = cookies.bake(extra_context=context)
    run_inside_dir("python craft test_package:install", str(result.project))


def test_can_import_package_in_masonite_namespace(cookies, context):
    """Generated project should pass black,
    for now only packages sources (src/*)"""
    result = cookies.bake(extra_context=context)

    test_command = "import masonite.{0}".format(context["pkg_name"])
    run_inside_dir("python -c '{0}'".format(test_command), str(result.project))
    assert result is not None
