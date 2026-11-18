#!/usr/bin/env bash
set -euo pipefail

# GitHub CLI 2.103.3, pinned to the official Linux amd64 release asset digest.
readonly version="2.103.3"
readonly archive="gh_${version}_linux_amd64.tar.gz"
readonly url="https://github.com/cli/cli/releases/download/v${version}/${archive}"
readonly expected_sha256="4c806978ffce1cec70853302a56d70ac6da4f19bae7adca4e1a8ab00633dd91d"

: "${RUNNER_TEMP:?RUNNER_TEMP must be set by GitHub Actions}"
: "${GITHUB_PATH:?GITHUB_PATH must be set by GitHub Actions}"

work_dir="$(mktemp -d "${RUNNER_TEMP}/gh-cli-install.XXXXXX")"
trap 'rm -rf "$work_dir"' EXIT

curl --fail --location --retry 3 --silent --show-error "$url" --output "$work_dir/$archive"
printf '%s  %s\n' "$expected_sha256" "$work_dir/$archive" | sha256sum --check --status

tar -xzf "$work_dir/$archive" -C "$work_dir"
source_binary="$work_dir/gh_${version}_linux_amd64/bin/gh"
test -x "$source_binary"

install_dir="$RUNNER_TEMP/gh-cli-pinned-bin"
mkdir -p "$install_dir"
install -m 0755 "$source_binary" "$install_dir/gh"
echo "$install_dir" >> "$GITHUB_PATH"

"$install_dir/gh" version | grep -F "gh version ${version} "
