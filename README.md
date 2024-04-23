# SUMMARY :

# IMPLEMENTATION STEPS :

1. **Color Space Conversion:** Convert the color host image from RGB to YIQ space to better match the human visual system.
2. **Wavelet Transformation:** Apply a three-level discrete wavelet transformation to the luminance component (Y) to produce four different frequency sub-bands.
3. **Singular Value Decomposition (SVD):** Perform SVD on these sub-bands.
4. **Watermark Processing:** Apply discrete wavelet transformation to the watermark image after scrambling encryption processing. This step prepares the watermark for embedding.
5. **Differential Evolution (DE) Optimization:** Use the DE algorithm to adaptively select the right scaling factors for embedding the watermark. This is a crucial step to balance invisibility and robustness.
6. **Embedding:** Modify the singular values of the Y component's sub-bands with those of the watermark's sub-bands, adjusted by the scaling factors determined through DE.
7. **Inverse Operations:** Conduct inverse SVD and inverse wavelet transformation to reconstruct the watermarked image in the YIQ space.
8. **Convert Back to RGB:** Transform the watermarked image back to RGB color space for the final output.

# IMPORTANT TERMS :

1. RGB : The RGB colour model is the most common colour model used in Digital image processing and openCV. The colour image consists of 3 channels. One channel each for one colour. Red, Green and Blue are the main colour components of this model. All other colours are produced by the proportional ratio of these three colours only. 0 represents the black and as the value increases the colour intensity increases.
2. **CMYK** : CMYK colour model is widely used in printers. It stands for Cyan, Magenta, Yellow and Black (key). It is a subtractive colour model. 0 represents the primary colour and 1 represents the lightest colour. In this model, point (1, 1, 1) represents black, and (0,0,0) represents white. It is a subtractive model thus the value is subtracted from 1 to vary from least intense to a most intense colour value.
3. **HSV:** The image consists of three channels. Hue, Saturation and Value are three channels. This colour model does not use primary colours directly. It uses colour in the way humans perceive them. HSV colour when is represented by a cone. Hue is a colour component. Since the cone represents the HSV model, the hue represents different colours in different angle ranges. Saturation as the name suggest describes the percentage of the colour. Sometimes this value lies in the 0 to 1 range. 0 being the grey and 1 being the primary colour. Saturation describes the grey colour. The value represents the intensity of the colour chosen. Its value lies in percentage from 0 to 100. 0 is black and 100 is the brightest and reveals the colour. HSV model is used in histogram equalization and converting grayscale images to RGB colour images.
4. **YIQ:** YIQ is the most widely colour model used in Television broadcasting. Y stands for luminance part and IQ stands for chrominance part. In the black and white television, only the luminance part (Y) was broadcast. The y value is similar to the grayscale part. The colour information is represented by the IQ part. YIQ model is used in the conversion of grayscale images to RGB colour images.

# MATHEMATICAL FORMULAES :

1. **Color Space Transformation from RGB to YIQ:**

   ![1712555754564](image/README/1712555754564.png)

2. **Inverse Color Space Transformation from YIQ to RGB:**

   ![1712555795124](image/README/1712555795124.png)

3. **Arnold Transform:**

   ![1712555840484](image/README/1712555840484.png)

4. **Singular Value Decomposition (SVD):**

   ![1712555892724](image/README/1712555892724.png)

5. **Differential Evolution Mutation:**

   ![1712555934553](image/README/1712555934553.png)

6. **Objective Function for Optimization:**

   ![1712555964240](image/README/1712555964240.png)

7. **Normalized Correlation (NC):**

   ![1712556001048](image/README/1712556001048.png)

8. **PSNR (Peak Signal to Noise Ratio):**

   ![1712556031724](image/README/1712556031724.png)

9. **Modification of Singular Values for Watermark Embedding:**

   ![1712556067906](image/README/1712556067906.png)
