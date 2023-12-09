import cv2
import numpy as np

def find_difference(image1, image2):
    # 加载图像
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    # 转换为灰度图像
    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    count_zeroes_listx = []
    count_zeroes_listy = []
    for i in range(-30, 30):
        translation_vector = (i, 0)  # x为正值表示右移，y为正值表示上移
        # 构建平移变换矩阵
        M = np.float32([[1, 0, translation_vector[0]], [0, 1, translation_vector[1]]])
        # 应用平移变换到原始图像
        gray_img2_new = cv2.warpAffine(gray_img2, M, gray_img2.shape[:2], flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP,borderValue=(255,255,255))

        # 计算图像的差异
        difference = cv2.absdiff(gray_img1, gray_img2_new)
        count_zeroes = np.sum(np.equal(difference, 255))  # 统计等于0的元素数量
        count_same = np.sum(np.equal(difference, 0))  # 统计等于0的元素数量
        #print(i,count_zeroes,count_same)
        count_zeroes_listx.append(count_zeroes)
    move_best_posx = count_zeroes_listx.index(min(count_zeroes_listx))-30


    for i in range(-30, 30):
        translation_vector = (move_best_posx, i)  # x为正值表示右移，y为正值表示上移
        # 构建平移变换矩阵
        M = np.float32([[1, 0, translation_vector[0]], [0, 1, translation_vector[1]]])
        # 应用平移变换到原始图像
        gray_img2_new = cv2.warpAffine(gray_img2, M, gray_img2.shape[:2], flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP,borderValue=(255,255,255))
        # 计算图像的差异
        difference = cv2.absdiff(gray_img1, gray_img2_new)
        count_zeroes = np.sum(np.equal(difference, 255))  # 统计等于0的元素数量
        count_same = np.sum(np.equal(difference, 0))  # 统计等于0的元素数量
        #print(i,count_zeroes,count_same)
        count_zeroes_listy.append(count_zeroes)

    move_best_posy = count_zeroes_listy.index(min(count_zeroes_listy))-30

    print("最佳位移矩阵为(%d,%d)"%(move_best_posx,move_best_posy))

    translation_vector = (move_best_posx, move_best_posy)  # x为正值表示右移，y为正值表示上移
    M = np.float32([[1, 0, translation_vector[0]], [0, 1, translation_vector[1]]])
    gray_img2_new = cv2.warpAffine(gray_img2, M, gray_img2.shape[:2], flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP,borderValue=(255, 255, 255))
    # 计算图像的差异
    difference = cv2.absdiff(gray_img1, gray_img2_new)
    count_zeroes = np.sum(np.equal(difference, 255))  # 统计等于0的元素数量
    count_same = np.sum(np.equal(difference, 0))  # 统计等于0的元素数量
    print("差异度为%d，相似度为%d"%(count_zeroes,count_same))


    #print(difference)
    # 显示差异图像
    cv2.imshow('Difference', difference)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image1_path = 'img\1.jpg'  # 替换成你的第一个图像路径
    image2_path = 'img\2.jpg'  # 替换成你的第二个图像路径
    find_difference(image1_path, image2_path)
