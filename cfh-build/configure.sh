#!/usr/bin/env bash
# CFH modification, 2026-11-07: configure the fork with its own complete branding assets.
set -euo pipefail
cd "$(dirname "$0")/.."
for asset in intro.png intro-highres.png logo.svg logo_inverted.svg logo-sc.svg logo-sc_inverted.svg about.svg donate1.png donate2.png; do
  if [ ! -s "cfh-brand/$asset" ]; then
    printf 'Missing CFH Office branding asset: %s\n' "$asset" >&2
    exit 1
  fi
done
exec ./autogen.sh --enable-release-build --with-product-name='CFH Office' --with-vendor='Coders for Humanity' --with-branding="$PWD/cfh-brand" "$@"