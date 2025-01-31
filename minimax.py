import numpy as np


def test_matrix(rowmat, colmat):
    rows_left = np.arange(rowmat.shape[0])
    cols_left = np.arange(colmat.shape[1])
    rows_tried = []
    cols_tried = []
    elim_hist = []

    while len(rows_tried) < len(rows_left) or len(cols_tried) < len(cols_left):
        do_row = np.random.randint(0, 2) > 0
        if do_row or len(cols_tried) == len(cols_left):
            row = np.random.choice(rows_left)
            if row in rows_tried:
                continue
            rows_tried.append(row)
            for r in rows_left:
                if r != row:
                    geq = np.sum(
                        rowmat[[r], :][:, cols_left] >= rowmat[[row], :][:, cols_left]
                    ) == len(cols_left)
                    g = (
                        np.sum(
                            rowmat[[r], :][:, cols_left]
                            > rowmat[[row], :][:, cols_left]
                        )
                        > 0
                    )
                    if geq and g:
                        rows_left = np.delete(rows_left, np.where(rows_left == row))
                        rows_tried = []
                        cols_tried = []
                        elim_hist.append((row, "row"))
                        break
        elif not do_row or len(rows_tried) == len(rows_left):
            col = np.random.choice(cols_left)
            if col in cols_tried:
                continue

            cols_tried.append(col)
            for c in cols_left:
                carr = colmat[rows_left, :]
                if c != col:
                    geq = np.sum(carr[:, [c]] >= carr[:, [col]]) == len(rows_left)
                    
                    g = np.sum(carr[:, [c]] > carr[:, [col]]) > 0
                    if geq and g:
                        print(carr[:, [c]])
                        print(carr[:, [col]])
                        cols_tried = []
                        rows_tried = []
                        cols_left = np.delete(cols_left, np.where(cols_left == col))
                        elim_hist.append((col, "col"))
                        break
    if len(rows_left) != 1 or len(cols_left) != 1:
        return rows_left, cols_left, elim_hist
    return None, None, None

def minimax(rm):
    rows = rm.shape[0]
    cols = rm.shape[1]

    mat = rm.copy()
    print("doing minimax: ")
    print(mat)
    while True:
        rowmins = np.min(mat, axis=1)
        print(rowmins)
        print(f"where rosmins: {np.where(rowmins == np.max(rowmins))[0]}")
        mat = mat[np.where(rowmins == np.max(rowmins))[0],:]
        print(f"mat after rowmins: {mat}")
        colmaxs = np.max(mat, axis=0)
        mat = mat[:,np.where(colmaxs == np.min(colmaxs))[0]]
        print(f"mat after colmaxes: {mat}")
        nr = mat.shape[0]
        nc = mat.shape[1]
        if nr == rows and nc == cols:
            break
        else:
            rows = nr
            cols = nc
        break
    return mat

if __name__ == "__main__":
    n_tried = 0
    n_with_ne = 0
    while True:
        if n_tried % 1000 == 0:
            print(f"tried: {n_tried}, with ne: {n_with_ne}")
        n_tried += 1
        rowmat = np.random.randint(0, 10, size=(3, 3))
        colmat = -rowmat.copy()#np.random.randint(0, 10, size=(3, 3))

        #rowmat = np.random.rand(2, 3)
        #colmat = np.random.rand(2, 3)
        rows,cols,eh = test_matrix(rowmat, colmat)
        if rows is None:
            continue
        print(rowmat)
        print(rows,cols,eh)
        
        rm = rowmat[rows,:][:,cols]
        print(rm)
        print(minimax(rm))  
        input()