import string

def convert_ineq_approx(tex_str):
    # reformat equations before splitting into LHS and RHS
    tex_str = tex_str.replace(r'\propto', '=')
    tex_str = tex_str.replace(r'\approx', '=')
    tex_str = tex_str.replace(r'\leq', '=')
    tex_str = tex_str.replace(r'\geq', '=')
    tex_str = tex_str.replace(r'\gg', '=')
    tex_str = tex_str.replace(r'\ll', '=')    
    tex_str = tex_str.replace(r'\\n', '')     
        
    return tex_str
    
def convert_str(tex_str):
    # Delete special commands
    tex_str = tex_str.replace(r'\partial', ' ')
    tex_str = tex_str.replace(r'\parder', ' ')
    tex_str = tex_str.replace(r'\dot{m}', 'Scav')
    tex_str = tex_str.replace(r'\right]', ')')
    tex_str = tex_str.replace(r'\left[', '(')
    tex_str = tex_str.replace(r'\right\}', ')')
    tex_str = tex_str.replace(r'\left\{', '(')    
    tex_str = tex_str.replace(r'\right', ' ')
    tex_str = tex_str.replace(r'\left', ' ')
    tex_str = tex_str.replace(r'\langle', ' ')
    tex_str = tex_str.replace(r'\rangle', ' ')
    tex_str = tex_str.replace(r'\overline{', '(')
    tex_str = tex_str.replace(r'\overline', ' ')
    tex_str = tex_str.replace(r'\widetilde{', '(')
    tex_str = tex_str.replace(r'\widetilde', ' ')
    tex_str = tex_str.replace(r'\Delta', ' ')
    tex_str = tex_str.replace(r'\sqrt{', '(') ### ATTENTION! Not correct...
    
    # Keep indices k, omega, Pi_ij, D_ij, P_ij, P_kk, Rij, R_ik, R_jk
    tex_str = tex_str.replace(r'_k', 'k')
    tex_str = tex_str.replace(r'_{k}', 'k')
    tex_str = tex_str.replace(r'_{\omega 2}', 'omega')
    tex_str = tex_str.replace(r'_{\omega2}', 'omega')
    tex_str = tex_str.replace(r'_\omega', 'omega')
    tex_str = tex_str.replace(r'_{\omega}', 'omega')
    tex_str = tex_str.replace(r'\Pi_{ij}', 'Piij')
    tex_str = tex_str.replace(r'D_{ij}', 'Dij')
    tex_str = tex_str.replace(r'P_{ij}', 'Pij')
    tex_str = tex_str.replace(r'P_{kk}', 'Pkk')
    tex_str = tex_str.replace(r'R_{ij}', 'Rij')
    tex_str = tex_str.replace(r'R_{ik}', 'Rik')
    tex_str = tex_str.replace(r'R_{jk}', 'Rjk')
    
    # Delete indices epsilon, epsilon1, epsilon2, mu, Phi, b1, b2, d, i, j, ij, ik, jk, kj, kl, t, t1, t2, v1, v_K, w, w1, 1, 1e, 2, 3, star, '
    tex_str = tex_str.replace(r'_\epsilon', ' ')
    tex_str = tex_str.replace(r'_{\epsilon}', ' ')
    tex_str = tex_str.replace(r'_{\epsilon1}', ' ')
    tex_str = tex_str.replace(r'_{\epsilon 1}', ' ')
    tex_str = tex_str.replace(r'_{\epsilon2}', ' ')
    tex_str = tex_str.replace(r'_{\epsilon 2}', ' ')
    tex_str = tex_str.replace(r'_\mu', ' ')
    tex_str = tex_str.replace(r'_{\mu}', ' ')
    tex_str = tex_str.replace(r'_\Phi', ' ')
    tex_str = tex_str.replace(r'_{\Phi}', ' ')
    tex_str = tex_str.replace(r'_{b1}', ' ')
    tex_str = tex_str.replace(r'_{b2}', ' ')
    tex_str = tex_str.replace(r'_d', ' ')
    tex_str = tex_str.replace(r'_{d}', ' ')
    tex_str = tex_str.replace(r'_i', ' ')
    tex_str = tex_str.replace(r'_{i}', ' ')
    tex_str = tex_str.replace(r'_j', ' ')
    tex_str = tex_str.replace(r'_{j}', ' ')
    tex_str = tex_str.replace(r'_{ij}', ' ')
    tex_str = tex_str.replace(r'_{ik}', ' ')
    tex_str = tex_str.replace(r'_{jk}', ' ')
    tex_str = tex_str.replace(r'_{kj}', ' ')
    tex_str = tex_str.replace(r'_{kl}', ' ')
    tex_str = tex_str.replace(r'_t', ' ')
    tex_str = tex_str.replace(r'_{t}', ' ')
    tex_str = tex_str.replace(r'_{t1}', ' ')
    tex_str = tex_str.replace(r'_{t2}', ' ')
    tex_str = tex_str.replace(r'_{v1}', ' ')
    tex_str = tex_str.replace(r'_{v_K}', ' ')
    tex_str = tex_str.replace(r'_v', ' ')
    tex_str = tex_str.replace(r'_l', ' ')
    tex_str = tex_str.replace(r'_w', ' ')
    tex_str = tex_str.replace(r'_{w}', ' ')
    tex_str = tex_str.replace(r'_{w1}', ' ')
    tex_str = tex_str.replace(r'^\star', ' ')
    tex_str = tex_str.replace(r'^{\star}', ' ')
    tex_str = tex_str.replace(r"'", ' ')
    tex_str = tex_str.replace(r'_1', ' ')
    tex_str = tex_str.replace(r'_{1}', ' ')
    tex_str = tex_str.replace(r'_{1e}', ' ')
    tex_str = tex_str.replace(r'_2', ' ')
    tex_str = tex_str.replace(r'_{2}', ' ')
    tex_str = tex_str.replace(r'_3', ' ')
    tex_str = tex_str.replace(r'_{3}', ' ')
    tex_str = tex_str.replace(r'_4', ' ')
    tex_str = tex_str.replace(r'_{4}', ' ')
    tex_str = tex_str.replace(r'_5', ' ')
    tex_str = tex_str.replace(r'_{5}', ' ')
    tex_str = tex_str.replace(r'_6', ' ')
    tex_str = tex_str.replace(r'_{6}', ' ')
    
    # Replace ^{ } by **
    tex_str = tex_str.replace(r'^2', '**2')
    tex_str = tex_str.replace(r'^{2}', '**2 ')
    tex_str = tex_str.replace(r'^{\frac{3}{2}}', '**(3/2)') ### ATTENTION! eval() cannot handle this
    tex_str = tex_str.replace(r'^{\frac{3}{4}}', '**(3/4)') ### ATTENTION! eval() cannot handle this
    
    # Replace \frac by /
    tex_str = tex_str.replace(r'\frac{', '(')
    tex_str = tex_str.replace('} {', ')/(')
    tex_str = tex_str.replace('}{', ')/(')
    tex_str = tex_str.replace('}', ')')
    tex_str = tex_str.replace('{', '(')

    # Delete superfluos whitespace
    tex_str = ' '.join(tex_str.split())
    tex_str = tex_str.replace('( ', '(')
    tex_str = tex_str.replace(' )', ')')
    tex_str = tex_str.replace(' + ', '+')
    tex_str = tex_str.replace(' +', '+')
    tex_str = tex_str.replace('+ ', '+')
    tex_str = tex_str.replace(' - ', '-')
    tex_str = tex_str.replace(' -', '-')
    tex_str = tex_str.replace('- ', '-')
    tex_str = tex_str.replace(' * ', '*')
    tex_str = tex_str.replace(' *', '*')
    tex_str = tex_str.replace('* ', '*')
    tex_str = tex_str.replace(' / ', '/')
    tex_str = tex_str.replace(' /', '/')
    tex_str = tex_str.replace('/ ', '/')
    
    # Replace empty brackets (e.g. if only \partial in numerator)
    tex_str = tex_str.replace('( )', '1')
    tex_str = tex_str.replace('()', '1')
    
    ### Insert multiplication sign where missing
    str_parts = [tex_str]
    start = 0
    for idx, char in enumerate(tex_str):
        # Break when reaching last character
        if idx+1 == len(tex_str):
            break
        # Split string when digit followed by letter
        if ((char in string.digits and tex_str[idx+1] in string.ascii_letters)
                # or when digit followed by ( or \ (escape character workaround!)
                or (char in string.digits and tex_str[idx+1] not in [' ', ')', '+', '-', '*', '/', ',', '.'] and tex_str[idx+1] not in string.ascii_letters)
                # or when letter followed by ( or \ (escape character workaround!)
                or (char in string.ascii_letters and tex_str[idx+1] not in [' ', ')', '+', '-', '*', '/', ',', '.'] and tex_str[idx+1] not in string.ascii_letters)
                # or when ) followed by digit, letter or \ (escape character workaround!)
                or (char == ')' and tex_str[idx+1] not in [' ', ')', '+', '-', '*', '/', ',', '.'])):
            str_parts.pop()
            str_parts.append(tex_str[start:idx+1].strip())
            str_parts.append(tex_str[idx+1:].strip())
            start = idx + 1
    # Join parts with multiplication sign
    tex_str = '*'.join(str_parts)
    # Insert multiplication sign between parentheses
    tex_str = tex_str.replace(')(', ')*(')
    # Also insert multiplication sign at remaining whitespace
    tex_str = tex_str.replace(' ', '*')
    
    # Delete \ from symbols
    tex_str = tex_str.replace(r'\alpha', 'alpha')
    tex_str = tex_str.replace(r'\beta', 'beta')
    tex_str = tex_str.replace(r'\delta', 'delta')
    tex_str = tex_str.replace(r'\epsilon', 'epsilon')
    tex_str = tex_str.replace(r'\kappa', 'kappa')
    tex_str = tex_str.replace(r'\mu', 'mu')
    tex_str = tex_str.replace(r'\nu', 'nu')
    tex_str = tex_str.replace(r'\omega', 'omega')
    tex_str = tex_str.replace(r'\Omega', 'Omega')
    tex_str = tex_str.replace(r'\Phi', 'Phi')
    tex_str = tex_str.replace(r'\rho', 'rho')
    tex_str = tex_str.replace(r'\sigma', 'sigma')
    tex_str = tex_str.replace(r'\sigmaomega', 'sigmaomega')
    tex_str = tex_str.replace(r'\tau', 'tau')
    tex_str = tex_str.replace(r'\zeta', 'zeta')
    
    return tex_str
