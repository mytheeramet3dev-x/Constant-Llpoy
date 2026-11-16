import Lake
open Lake DSL

package constantLlapoy where
  version := v!"0.1.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4" @
  "96f6b8b8e029545577421f198a89fb174a4d62e6"

@[default_target]
lean_lib ConstantLlapoy
