import cv2
import numpy as np
import pywt
from scipy.linalg import svd, diagsvd
from scipy.optimize import differential_evolution
from target import target_func

def rgb_to_yiq(rgb_image):
    transformation_matrix = np.array([[0.299, 0.587, 0.114],
                                      [0.596, -0.275, -0.321],
                                      [0.212, -0.523, 0.311]])
    yiq_image = np.dot(rgb_image, transformation_matrix.T)
    return yiq_image

def yiq_to_rgb(yiq_image):
    transformation_matrix = np.array([[1.000, 0.956, 0.620],
                                      [1.000, -0.272, -0.647],
                                      [1.000, -1.108, 1.703]])
    rgb_image = np.dot(yiq_image, np.linalg.inv(transformation_matrix.T))
    return rgb_image

def apply_dwt(image):
    coeffs = pywt.dwt2(image, 'haar')
    cA, (cH, cV, cD) = coeffs
    return coeffs

def apply_svd(matrix):
    U, S, Vt = svd(matrix, full_matrices=False)
    return U, S, Vt

def watermark_embedding(U, S, Vt, watermark_matrix, scale_factor):
    # print(f'S: {S}')
    # print(f'SF: {scale_factor}')
    # print(f'WM: ${watermark_matrix}')
    S_w = (scale_factor * watermark_matrix) + S
    watermarked_matrix = np.dot(U, np.dot(diagsvd(S_w, *U.shape), Vt))
    return watermarked_matrix

def differential_evolution_optimization(bounds):
    result = differential_evolution(target_func, bounds)
    return result.x

def main():
    # Load your images
    host_image = cv2.imread('./assets/host_image.png')
    watermark_image = cv2.imread('./assets/watermark_image.png', cv2.IMREAD_GRAYSCALE)
    
    # Convert to YIQ color space
    host_image_yiq = rgb_to_yiq(host_image / 255.0)  # Normalized

    # Apply DWT to luminance channel
    coeffs = apply_dwt(host_image_yiq[:, :, 0])
    cA, (cH, cV, cD) = coeffs

    # Apply SVD
    U, S, Vt = apply_svd(cA)
    
    # Example scale factor (use DE to find optimal)
    scale_factor = 0.05  # This should be optimized
    
    # Watermark embedding
    watermarked_cA = watermark_embedding(U, S, Vt, watermark_image, scale_factor)
    
    # Inverse DWT and SVD operations, then convert back to RGB (not shown here)

if __name__ == "__main__":
    main()