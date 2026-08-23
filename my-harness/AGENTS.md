CONSTRAINT 1: use it as a map, not a handbook; point to the exact file that owns each topic; do not keep explanations that belong in deeper docs; keep it short enough to read on every tasks.
CONSTRAINT 2: keep only what this repo is, what to read first, common commands, hard rules, where deeper docs live.
CONSTRAINT 3: Use nested AGENTS.md only where there are genuinely local rules. For example, simulator/ may need a AGENTS.md to discuss `never expose hidden WorldState fields through Observation....`

`docs/*/__init__.md` -- Under every folder, there is an `__init__.md` that describes the purpose of the folder and what to read first. These files are meant to be read in order, and they are not meant to be executed.

