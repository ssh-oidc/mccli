.. _development:

For developers
==============

Branching model
---------------

- ``develop`` is the development branch. All day-to-day work lands here.
- ``main`` is the release branch. It advances only via release pull
  requests ``develop`` → ``main`` — never by direct pushes.
- ``vX.Y.Z`` tags are created on ``main`` when a release is published
  (see below).

Releasing
---------

The version is tracked in a single place:

- ``mccli/VERSION`` (read by ``setup.cfg`` via ``version = file:
  mccli/VERSION``), kept in sync by ``bump2version`` (configured in
  ``.bumpversion.cfg``).


When to bump
^^^^^^^^^^^^

Bump on ``develop`` as part of the release, once all feature work is
merged and CI is green::

    bump2version [patch|minor|major]

Use ``patch`` for bug fixes and dependency updates, ``minor`` for new
backwards-compatible functionality, and ``major`` for breaking changes.

Rules:

- Never hand-edit the version string. Hand edits desynchronise
  ``.bumpversion.cfg`` and the tool stops working.
- The tool never tags (``tag = False``). ``vX.Y.Z`` tags are created via
  the GitHub release (see below).

Release checklist
^^^^^^^^^^^^^^^^^

1. All feature pull requests merged to ``develop``, GitHub CI (tox
   matrix) green.
2. ``bump2version [patch|minor|major]`` on ``develop`` (commits
   automatically).
3. Open pull request ``develop`` → ``main``, review, merge.
4. If the CI on ``main`` is green,
   create a release on GitHub from the release (the merge commit on
   ``main``): enter ``vX.Y.Z`` as a new tag — publishing the release
   creates the tag, which triggers the PyPI publish (TestPyPI and PyPI).
   Add release notes describing the changes since the previous release.
