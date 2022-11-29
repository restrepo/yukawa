#!/usr/bin/env python3
r'''
Tools for chiral fermions
'''


def get_massive_fermions(l,s,ps=[]):
    '''
    For a given scalar Abelian charge `s`, build the 
    fermion non-zero determinant mass matrix from their
    Abelian charges in `l`, and returns the input `s` and 
    the non-zero mass entries.
    Returns an empty dictionary otherwise.
    
    The list of combinations on pairs of `l` can be given in `ps`,
    otherwise it is internally calculated.
    
    Example:
        l = [1, 3, 4, 6, -7, -8, -13, 14]
        s = 7
        ps = [(3,4),(6,-13),(1,6),(-7,14),(1,-8)]
        # If necessary temove [1,6] because have is fully contained 
        # in the intersections with others
        [1, 3, 4, 6, -7, -8, -13, 14] → [(3,4),(6,-13),(-7,14),(1,-8)]
        [1, 6, -7, -8, -13, 14] → [(6,-13),(-7,14),(1,-8)]
        [1, -7, -8, 14] → [(-7,14),(1,-8)]
        [1, -8] → [(1,-8)]
        [] → []
        
        returns:
        {'s':7, '\psi':[(3,4),(6,-13),(1,6),(-7,14),(1,-8)]}

    '''
    sltn={}
    if not ps:
        ps = list(set(itertools.combinations_with_replacement(l,2)))
    msv = [p for p in ps if abs(sum(p))==s]
    lmsv=[x for sublist in msv for x in sublist]
    massives=set(lmsv)        
    massless=set(l).difference(massives)
    if not massless:
        # ========= Quality check =======================
        # Check that all the elements of l can be removed
        for INTERSECTIONS in [False,True]:
            msvp=msv.copy()
            lp=l.copy()
            if INTERSECTIONS:
                msvp = remove_double_intersection_pairs(msvp,l)
            for msvp in itertools.permutations(msvp.copy()):
                msvp=list(msvp)
                lp=get_real_massless(l,msvp)
                if not lp:
                    break # found real massless
            if not lp: # double break for INTERSECTIONS
                break # found real massless
                    
        
        if not lp:
            sltn['S']=s
            sltn['ψ']=msv
        return sltn
assert get_hidden_fermions([2, 4, 4, 5

if __name__ == '__main__':
    r'''
    Checks
    '''
    get_massive_fermios([1, 3, 4, 6, -7, -8, -13, 14],7)
