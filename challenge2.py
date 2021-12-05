"""
this program aim for determine 3 consecutive point 
that construct a line in a matrices
"""
# shape for matrices
shape = (4, 4)

# construct a matrice from input data
mat = []
for row in range(shape[0]):
    ls_row = []
    for col in range(shape[-1]):
        val = input(f'insert value in row {row+1} col {col+1}:\t')
        ls_row.append(val)
    mat.append(ls_row)

# mat = [
#     ['x', 'd', 'i', 'p'],
#     ['d', 'i', 'p', 'p'],
#     ['x', 'p', 'x', 'x'],
#     ['x', 'p', 'x', 'x']
# ]

mat_transpose = []
check = 'dip'
ls_check = []

for i, val in enumerate(mat):
    col = []
    for j,_ in enumerate(val):
        # horizontal check
        if j <= len(val) - len(check):
            if (val[j] == 'd') & (val[j+1] == 'i') & (val[j+2] == 'p'):
               ls_check.append(1)
            else: pass
        
        col.append(mat[j][i])
    mat_transpose.append(col)

for i, val in enumerate(mat_transpose):
    for j,_ in enumerate(val):
        # vertical check
        
        if j <= len(val) - len(check):
            if (val[j] == 'd') & (val[j+1] == 'i') & (val[j+2] == 'p'):
               ls_check.append(1)
            else: pass

print(mat)
print(mat_transpose)
print(len(ls_check))