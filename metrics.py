def get_confusion_matrix(label, pred):
    # 3x3 matrix: POS,NEG,NEU
    matrix = [[0,0,0],[0,0,0],[0,0,0]]
    
    for l, p in zip(label, pred):
        matrix[l][p] += 1
        
    return matrix