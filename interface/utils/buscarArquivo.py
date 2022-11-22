def search(name):
    import os

    path = name
    imgs = []
    pcd = []
    print("Buscando arquivos")
    for (root, dirs, files) in os.walk(path, topdown=True):
        for file in files:
            f_type = file.split(".")
            if f_type[1] == "png":
                imgs.append(file)
            elif f_type[1] == "pcd":
                pcd.append(file)
    if len(imgs) == 0 or len(pcd) == 0:
        print("Pasta indicada inválida")
        exit()
    else:
        print("!......")
        return imgs, pcd
