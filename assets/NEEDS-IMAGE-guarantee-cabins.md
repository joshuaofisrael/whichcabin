# Needs image: guarantee cabins

Do not merge this branch until the thumbnail file is in the repo and the launch build is regenerated.

- Bank file: `/workspace/image-bank/which/cruise-cabin-keycard-door.png`
- Repo path the build reads: `assets/cruise-cabin-keycard-door.png`
- Page: `/guides/guarantee-cabins/`
- Scene: a cruise cabin door and keycard lock in ordinary corridor light, camera look. No logos, no readable text, no real faces, no glossy illustration.
- When the file is present, `python3 _build/build.py --launch` adds the photo, captioned AI-generated and linked to `/image-policy/`.
