if exists("b:current_syntax")
    finish
endif

syn keyword oxianKwds print this
syn keyword oxianStatements return break breakall breakto continue assert
syn keyword oxianModifiers inline volatile
syn keyword oxianStrctures class enum namespace
syn keyword oxianLabels case default
syn keyword oxianVarDecls var const
syn keyword oxianConditionals if else switch
syn keyword oxianLoops while for
syn keyword oxianTypes char uint8 uint16 uint32 uint64 sint8 sint16 sint32 sint64 float bool double void

syn match oxianComment "//.*$"
syn match oxianComment "/\*\_.\{-}\*/"

syn match oxianString "\"\_.\{-}\""
syn match oxianString "'\_.\{-}'"
syn match oxianChar "c\".\""
syn match oxianChar "c'.'"

syn keyword oxianBool true false
syn keyword oxianConstant null

syn match oxianNumber "\<\d\+\>"
syn match oxianNumber "\<0o[0-7]\+\>"
syn match oxianNumber "\<0b[01]\+\>"
syn match oxianNumber "\<0x[0-9a-f]\+\>"
syn match oxianNumber "\<[0-9.]\+\>"

syn keyword oxianOperator ? : ! + - * / % = > < ~ & \| ^ ++ -- >> << && \|\| == += -= *= /= != >= <= %= <<= >>= &= \|= ^=

syn match oxianError "c'[^']\{-2,}'"
syn match oxianError "c\"[^"]\{-2,}\""

let b:current_syntax = "oxian"

hi def link oxianComment Comment
hi def link oxianKwds Keyword
hi def link oxianStatements Statement
hi def link oxianModifiers Keyword
hi def link oxianStrctures Structure
hi def link oxianLabels Label
hi def link oxianVarDecls Keyword
hi def link oxianConstant Constant
hi def link oxianConditionals Conditional
hi def link oxianLoops Repeat
hi def link oxianTypes Type
hi def link oxianOperator Type
hi def link oxianString String
hi def link oxianChar Character
hi def link oxianNumber Number
hi def link oxianBool Boolean
hi def link oxianFloat Float
hi def link oxianError Error
