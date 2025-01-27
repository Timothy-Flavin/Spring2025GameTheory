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
                        cols_tried = []
                        cols_left = np.delete(cols_left, np.where(cols_left == col))
                        elim_hist.append((col, "col"))
                        break
    if len(rows_left) == 1 and len(cols_left) == 1:
        return str(rows_left[0]) + str(cols_left[0]), elim_hist
    return None, None


if __name__ == "__main__":
    n_tried = 0
    n_with_ne = 0
    while True:
        if n_tried % 1000 == 0:
            print(f"tried: {n_tried}, with ne: {n_with_ne}")
        n_tried += 1
        rowmat = np.random.randint(0, 10, size=(2, 3))
        colmat = np.random.randint(0, 10, size=(2, 3))

        rowmat = np.random.rand(2, 3)
        colmat = np.random.rand(2, 3)
        first_key, eho = test_matrix(rowmat, colmat)
        if first_key is None:
            continue
        n_with_ne += 1
        d = {first_key: 1}
        for i in range(20):
            k2, eh = test_matrix(rowmat, colmat)
            if k2 is not None and k2 not in d:
                print(f"tried: {n_tried}, with ne: {n_with_ne}")
                print(d)
                print(k2)
                print(rowmat)
                print(colmat)
                print("we got one!!!")
                print(eh)
                print(eho)
                input()
