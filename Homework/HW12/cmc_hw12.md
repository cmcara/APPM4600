# Homework 12 - Charlie Caravati

> # 1

(i) $2x_1-6 \alpha x_2 = 3$

(ii) $3 \alpha x_1 - x_2 = \frac{3}{2}$

> (a) Value(s) of $\alpha$ for which the system has no solutions

$\begin{bmatrix} 2 & -6\alpha \\ 3\alpha & -1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 3 \\ \frac{3}{2} \end{bmatrix}$

This will not have unique solutions when the determinant is equal to 0.

$det(A) = (2)(-1) - (-6\alpha)(3\alpha) = 0$

$-2 + 18\alpha^2 = 0 \to 18\alpha^2 = 2 \to \alpha^2 = \frac{1}{9}$

$\alpha = \pm \frac{1}{3}$

When $$\alpha = - \frac{1}{3}$

(i) gives $2x_1-6 (-\frac{1}{3}) x_2 = 3$

$2x_1+2 x_2 = 3$

(ii) gives $3 (-\frac{1}{3}) x_1 - x_2 = \frac{3}{2}$

$- x_1 - x_2 = \frac{3}{2}$ mult by -2 gives 

$2x_1+2 x_2 = -3$

Thus when $\alpha = -\frac{1}{3}$ the system 

$2x_1+2 x_2 = 3$

$2x_1+2 x_2 = -3$

has no solutions.

> (b) Value(s) of $\alpha$ for which the system has infinite solutions

Testing the other critical values $\alpha = \frac{1}{3}$ gives 

(i) gives $2x_1-6 (\frac{1}{3}) x_2 = 3$

$2x_1-2 x_2 = 3$

(ii) gives $3 (\frac{1}{3}) x_1 - x_2 = \frac{3}{2}$

$x_1 - x_2 = \frac{3}{2}$ mult by -2 gives 

$2x_1+2 x_2 = 3$

Which match meaning the system has infinite solutions when $\alpha = \frac{1}{3}$.

> (c)

For $\alpha \neq \pm \frac{1}{3}$

$\begin{bmatrix} 2 & -6\alpha \\ 3\alpha & -1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 3 \\ \frac{3}{2} \end{bmatrix}$

$det(A) = 18\alpha^2 -2$

$x_1 = \frac{det(A_1)}{det(A)}$

$A_1 = \begin{bmatrix} 3 & -6\alpha \\ \frac{3}{2} & -1 \end{bmatrix}$

$det(A_1) = (3)(-1) - (-6\alpha)(\frac{3}{2}) = -3 + 9\alpha = 9\alpha - 3$

$x_1 = \frac{9\alpha - 3}{18\alpha^2 -2} = \frac{3(3\alpha - 1)}{2(3\alpha -1)(3\alpha + 1)} = \frac{3}{6\alpha + 2}$

$x_2 = \frac{det(A_2)}{det(A)}$

$A_2 = \begin{bmatrix} 2 & 3 \\ 3\alpha & \frac{3}{2} \end{bmatrix}$

$det(A_2) = (2)(\frac{3}{2}) - (3)(3\alpha) = 3 - 9\alpha$

$x_2 = \frac{3 - 9\alpha}{18\alpha^2 -2} = \frac{-3(3\alpha - 1)}{2(3\alpha -1)(3\alpha + 1)} = -\frac{3}{6\alpha + 2}$

$x_1 = \frac{3}{6\alpha + 2}$

$x_2 = -\frac{3}{6\alpha + 2}$

> ## 2.

$Ax = b$ where $A \in \mathbb{R}^{nxn}$ is a tridiagonal matrix 

> (a)

$A = \begin{bmatrix} a_1 & c_1 & 0 \\ b_2 & a_2 & c_2 \\ 0 & b_3 & a_3 \end{bmatrix}$

Choosing L as lower bidiagonal and U as upper bidiagonal to preserve tridiagonal of A and setting LU = A gives

$L = \begin{bmatrix} 1 & 0 & 0 \\ l_2 & 1 & 0 \\ 0 & l_3 & 1 \end{bmatrix}$

$U = \begin{bmatrix} u_1 & c_1 & 0 \\ 0 & u_2 & c_2 \\ 0 & 0 & u_3 \end{bmatrix}$

$LU = \begin{bmatrix} 1 & 0 & 0 \\ l_2 & 1 & 0 \\ 0 & l_3 & 1 \end{bmatrix} \begin{bmatrix} u_1 & c_1 & 0 \\ 0 & u_2 & c_2 \\ 0 & 0 & u_3 \end{bmatrix} = \begin{bmatrix} u_1 & c_1 & 0 \\ l_2u_1 & l_2c_1 + u_2 & c_2 \\ 0 & l_3u_3 & l_3c_2+u_3 \end{bmatrix}$

$u_1 = a_1$

$c_1 = c_1$

$l_2u_1 = b_2 \to l_2 = \frac{b_2}{u_1}$

$l_2c_1 + u_2 = a_2 \to u_2 = a_2 - l_2c_1$

$c_2 = c_2$

$l_3u_2 = b_3 \to l_3 = \frac{b_3}{u_2}$

$l_3c_2 + u_3 = a_3 \to u_3 = a_3 - l_3c_2$

By computing the pieces to L and U as 

$u_1 = a_1$

$l_2 = \frac{b_2}{u_1}$

$u_2 = a_2 - l_2c_1$

$l_3 = \frac{b_3}{u_2}$

$u_3 = a_3 - l_3c_2$

Which takes advantage of the sparsity to only compute only the non-zero tridiagonal entries.

> (b)

For a general n we can follow this pattern:

$u_1 = a_1$ 

for $j \geq 2$:

$l_j = \frac{b_j}{u_{j-1}}$

then

$u_j = a_j - l_jc_{j-1}$

for every $j \geq 2$ to populate L and U.

> (c)

This is much less expensive than standard Gaussian elimination because it requires significantly fewer operations to populate L and U. Because all other entries except the tridiagonal are zero, there are only 2 or 3 calculations needed for each row. This leads to $O(n)$ steps vs $O(n^3)$ for traditional Gaussian elimination.

> # 3.

$6x + 2y + 2z = -2$

$2x+ \frac{2}{3}y + \frac{1}{3}z = 1$

$x + 2y - z = 0$

> (a)

verify $(x, y, z) = (2.6, -3.8, -5)$ is the exact solution

$6(2.6) + 2(-3.8) + 2(-5) = 15.6 -7.6 -10 -2$ confirmed

$2(2.6)+ \frac{2}{3}(-3.8) + \frac{1}{3}(-5) = 5.2 + \frac{2}{3}(-3.8) + \frac{1}{3}(-5)= 1$ confirmed

$(2.6) + 2(-3.8) - (-5) = 2.6 - 7.6 + 5 = 0$ confirmed

> (b)

A = $\begin{bmatrix} 6.000 & 2.000 & 2.000 & \mid & -2.000 \\  2.000 & 0.6667 & 0.3333 & \mid & 1.000 \\  1.000 & 2.000 & -1.000 & \mid & 0.000 \end{bmatrix}$

A = $\begin{bmatrix} 6.000 & 2.000 & 2.000 & \mid & -2.000 \\  0 & 0.6667-.3333(2.000) & 0.3333-.3333(2.000) & \mid & 1.000 - .3333(-2.000) \\  0 & 2.000 - 2.000(.1667) & -1.000 - 2.000(.1667) & \mid & 0.000 -(-2.000)(.1667)\end{bmatrix}$

A = $\begin{bmatrix} 6.000 & 2.000 & 2.000 & \mid & -2.000 \\  0 & 0.0001 & -0.3333 & \mid & 1.667 \\  0 & 1.667 & -1.333 & \mid & 0.3334 \end{bmatrix}$

$\frac{1.667}{.0001} = 16670$

A = $\begin{bmatrix} 6.000 & 2.000 & 2.000 & \mid & -2.000 \\  0 & 0.0001 & -0.3333 & \mid & 1.667 \\  0 & 0 & -1.333 - (16670)(-.3333) & \mid & 0.3334 - (16670)(1.667) \end{bmatrix}$

$A = \begin{bmatrix} 6.000 & 2.000 & 2.000 & \mid & -2.000 \\  0 & 0.0001 & -0.3333 & \mid & 1.667 \\  0 & 0 & 5555 & \mid & -27710 \end{bmatrix}$

$5555z = -27710 \ to z = \frac{-27710}{5555} = -4.988$

$.0001y - .3333(-4.988) = 1.667 \to .0001y = 1.667 - 1.663 \to y = \frac{.004}{.0001} = 40$

$6.000x + 2(40.00) + 2(-4.988) = -2.000 \to 6.000x +80 -9.976 = 6.000x + 70.02 = -2.000 \to 6.000x = -72.02$

$x = \frac{-72.02}{6.000} = -12.00$

$(x, y, z) = (-12, 40, -4.988)$ which is far off from our true solution $(2.6, -3.8, -5)$

> (c)

From part (b) we got 

A = $\begin{bmatrix} 6.000 & 2.000 & 2.000 & \mid & -2.000 \\  0 & 0.0001 & -0.3333 & \mid & 1.667 \\  0 & 1.667 & -1.333 & \mid & 0.3334 \end{bmatrix}$

pivoting gives

A = $\begin{bmatrix} 6.000 & 2.000 & 2.000 & \mid & -2.000 \\  0 & 1.667 & -1.333 & \mid & 0.3334 \\ 0 & 0.0001 & -0.3333 & \mid & 1.667  \end{bmatrix}$

$\frac{.0001}{1.667} = .00005999 = 5.999 \times 10^{-5}$

A = $\begin{bmatrix} 6.000 & 2.000 & 2.000 & \mid & -2.000 \\  0 & 1.667 & -1.333 & \mid & 0.3334 \\ 0 & 0 & -0.3333 - (.00005999)(-1.333) & \mid & 1.667 - (.00005999)(.3334) \end{bmatrix}$

A = $\begin{bmatrix} 6.000 & 2.000 & 2.000 & \mid & -2.000 \\  0 & 1.667 & -1.333 & \mid & 0.3334 \\ 0 & 0 & -.3332 & \mid & 1.667 \end{bmatrix}$

Solving:

$-.3332z = 1.667 \to z = \frac{1.667}{-.3333} = -5.003$

$z = -5.003$

$1.667y - 1.333(-5.003) = .3334 \to 1.667y = .3334 - 6.669 \to y = \frac{-6.336}{1.667}$

$y = -3.801$

$6.000x + 2(-3.801) + 2(-5.003) = -2.000 \to 6.000x - 17.61 = -2.000 \to x = \frac{15.61}{6.000}$

$x = 2.602$

$(x, y, z) = (2.602, -3.801, -5.003)$ 

> (d)

$(x, y, z) = (2.602, -3.801, -5.003)$ from pivoting the matrix is much closer to the true solution (2.6, -3.8, -5) than (-12, 40, -4.988) which suffers from catastrophic cancellation without pivoting. Pivoting is the more stable and accurate method.