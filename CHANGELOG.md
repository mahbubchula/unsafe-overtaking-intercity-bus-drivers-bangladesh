# Changelog

This file records repository and research-document states. It follows a Keep a Changelog-style structure, but research-document status takes precedence over semantic-version labels.

## Unreleased

### Added

- Local repository structure and governance documentation.
- Privacy-focused ignore rules and repository attributes.
- Planned analysis-directory documentation.
- Read-only validation and manifest scripts.
- Safe continuous-integration checks that tolerate explicitly unavailable research documents during repository preparation.

### Document status

- Proposal-review version: not available for verification.
- Expert-review version: not available for verification.
- Cognitive-review version: not available for verification.
- Pilot version: not available for verification.
- Ethics-authorized version: not available for verification; no authorization claimed.
- Administered version: not available for verification; no administration claimed.
- Archived thesis version: not available for verification.

## Version policy

Pre-administration repository versions may use `v0.x.y-<stage>` labels, such as `v0.1.0-proposal`, only when the named stage is supported by the archived documents. Do not infer a stage from a filename alone.

The final administered package must bind the English questionnaire, Bangla questionnaire, master codebook, item justification, and relevant thesis appendix to one immutable Git commit. A release tag may be created only after the status and contents have been reviewed and confirmed. The tag or commit SHA must be recorded in the version-history documentation and referenced from the thesis appendix.

No release tag has been created.
