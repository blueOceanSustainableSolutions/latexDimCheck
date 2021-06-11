import string

def prepare_latex(tex_str):
    # reformat equations before sympy latex parser
    tex_str = tex_str.replace(r'\parder', '\\frac') # needed for proper dimensions
    tex_str = tex_str.replace(r'\matder', '\\frac') # needed for proper dimensions
    tex_str = tex_str.replace('\n', '')     
    tex_str = tex_str.replace('\t', '')
    tex_str = tex_str.replace('\langle', '')
    tex_str = tex_str.replace('\\rangle', '')
    tex_str = tex_str.replace('.', '')
    tex_str = tex_str.replace(',', '')
    tex_str = tex_str.replace("'", '')
    tex_str = tex_str.replace('\limits', '')
    tex_str = tex_str.replace(r'\propto', '=')
    tex_str = tex_str.replace(r'\approx', '=')
    tex_str = tex_str.replace(r'\leq', '=')
    tex_str = tex_str.replace(r'\geq', '=')
    tex_str = tex_str.replace(r'\gg', '=')
    tex_str = tex_str.replace(r'\ll', '=')    
    tex_str = tex_str.replace(r'\begin{split}', '')    
    tex_str = tex_str.replace(r'\end{split}', '')
    tex_str = tex_str.replace(r'\&', '')    
    
    
    return tex_str
    
