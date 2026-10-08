# 05 — Linear algebra: vectors, matrices, eigenvalues

**Read this if:** "eigenvalue", "symmetric matrix", "positive definite" or
"covariance matrix" are not second nature.

## 1. Vectors

A **vector** $v=(v_1,\dots,v_n)$ is a list of $n$ numbers. Two operations:
- **addition:** componentwise, $(u+v)_i=u_i+v_i$;
- **scalar multiplication:** $(\alpha v)_i=\alpha v_i$.

**Dot product:** $u\cdot v=\sum_{i=1}^n u_iv_i$. **Length (norm):**
$\left\|v\right\|=\sqrt{v\cdot v}$. **Orthogonal** = perpendicular = $u\cdot v=0$.

**Orthonormal set** $\{e_1,\dots,e_n\}$: $e_i\cdot e_j=\delta_{ij}$ ("length 1, all
mutually perpendicular"). In $\mathbb R^n$ such a set is a **basis**: every vector
can be uniquely written $v=\sum_i(v\cdot e_i)e_i$ — you read off the coordinates by
projecting. **Gram–Schmidt** is the recipe that turns any independent list into an
orthonormal one (used for degenerate kernels in Exercise 26/27).

## 2. Matrices

An $n\times m$ **matrix** $A$ is a rectangular array; $A_{ij}$ is row $i$, column
$j$. Matrix–vector product: $(Av)_i=\sum_j A_{ij}v_j$ — a linear rule transforming
vectors. **Transpose** $A^\top$: $(A^\top)_{ij}=A_{ji}$ (flip about the diagonal).
Facts you must have: $(AB)^\top=B^\top A^\top$, $(AB)C=A(BC)$, but in general
$AB\ne BA$.

**Special matrices:** **symmetric** ($A=A^\top$) — the self-adjoint case of file 06;
**diagonal** (only $A_{ii}\ne0$); **identity** $I$ ($Iv=v$);
**orthogonal** ($Q^\top Q=I$, i.e. $Q^{-1}=Q^\top$; rotations/reflections, they
preserve lengths).

## 3. Eigenvalues and eigenvectors

**In words.** Most matrices *rotate and stretch* vectors. Eigenvectors are the
special directions that are **only stretched** (not rotated).

**Exactly.** $\lambda$ is an **eigenvalue** with **eigenvector** $v\ne0$ if
$$\boxed{\ Av=\lambda v\ }$$
i.e. "applying $A$ to $v$ merely multiplies its length by $\lambda$". To find them,
solve $\det(A-\lambda I)=0$ (the **characteristic equation**); each solution $\lambda$
then gives $v$ from $(A-\lambda I)v=0$.

*Worked 1.* $A=\begin{pmatrix}2&0\\0&3\end{pmatrix}$:
$\det(A-\lambda I)=(2-\lambda)(3-\lambda)=0\Rightarrow\lambda=2,3$, with
eigenvectors $(1,0)$ and $(0,1)$.

*Worked 2.* $A=\begin{pmatrix}0&1\\1&0\end{pmatrix}$:
$\det\begin{pmatrix}-\lambda&1\\1&-\lambda\end{pmatrix}=\lambda^2-1=0\Rightarrow
\lambda=\pm1$, eigenvectors $(1,1)$ ($\lambda=1$) and $(1,-1)$ ($\lambda=-1$).

**Interpretation used in the chapter.** In the Karhunen–Loève expansion, the
eigenvalue $\lambda_n$ is *how much variance* lives in the direction $e_n$: bigger
$\lambda_n$ = more important mode.

## 4. The spectral theorem (the theorem that makes this chapter work)

> **If $A$ is real and symmetric, then**
> 1. all eigenvalues are **real**;
> 2. eigenvectors for **different** eigenvalues are **orthogonal**;
> 3. there is an **orthonormal basis** of eigenvectors $q_1,\dots,q_n$, so
>    $$A=Q\Lambda Q^\top,\qquad \Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n),$$
>    and $A$ acts as "rotate, stretch, rotate back".

**Proof sketch of (2):** $\lambda_1(q_1\cdot q_2)=(Aq_1)\cdot q_2
=q_1^\top A^\top q_2=q_1^\top Aq_2=q_1\cdot(Aq_2)=\lambda_2(q_1\cdot q_2)$, so
$(\lambda_1-\lambda_2)(q_1\cdot q_2)=0$. *The identical argument, with $\int$ in
place of $\sum$, is Exercise 20's last part (file 06).*

**Consequence:** a symmetric $A$ can always be written
$A=\sum_{k}\lambda_kq_kq_k^\top$, a sum of rank-one pieces — the discrete version of
the Karhunen–Loève / Mercer expansion (files 06 and 07).

## 5. Trace and determinant

- $\operatorname{tr}A=\sum_iA_{ii}$ (**trace**). Key facts:
  $\operatorname{tr}A=\sum_i\lambda_i$, $\operatorname{tr}(AB)=\operatorname{tr}(BA)$.
- $\det A=\prod_i\lambda_i$; $\det(AB)=\det A\det B$.
- **(1.32)-style identity:** summing the eigenvalues of $A$ gives $\operatorname{tr}A$;
  for a kernel this becomes $\int R(t,t)dt$ — that is Exercise 22 (file 06 §6).

## 6. Positive (semi-)definite

$A$ is **positive semi-definite (PSD)** if for **every** vector $v$,
$$v^\top Av\ \ge\ 0 .$$
**Positive definite** if the inequality is strict for $v\ne0$. By §4, $A$ PSD
$\iff$ all eigenvalues $\ge0$.

**A covariance matrix is always PSD.** Indeed, for $Y=\sum_i v_iX_i$,
$$v^\top\Sigma v=\sum_{i,j}v_iv_j\operatorname{Cov}(X_i,X_j)
=\operatorname{Var}(Y)\ge0 .$$
*This is exactly the trick in Exercise 20 (file 06 §3) with a sum replaced by an
integral.* PSD is precisely the condition a covariance kernel must satisfy
(file 04 §6).

## 7. Cholesky decomposition (needed for simulating, file 08)

If $\Gamma$ is symmetric positive definite, there is a lower-triangular $L$ with
$$\Gamma=LL^\top .$$
**Why we care:** to simulate a Gaussian vector with covariance $\Gamma$, take iid
standard normals $\zeta$, and set $X=L\zeta$; then
$\operatorname{Cov}(X)=L\operatorname{Cov}(\zeta)L^\top=LL^\top=\Gamma$. That is the
sampler used in `1_4.py` and described in file 08 (§T2).

## 8. Quadratics: completing the square

Used to integrate Gaussian densities. For a $>0$:
$$ax^2+bx+c=a\Big(x+\frac{b}{2a}\Big)^2+c-\frac{b^2}{4a}.$$
*Worked:* $x^2-4x=(x-2)^2-4$, so $\int e^{-(x^2-4x)}dx=e^{4}\int e^{-(x-2)^2}dx
=e^{4}\sqrt{\pi}$. Combining this with the Gaussian integral in file 01 §6 is how
$\mathbb E e^{sX}$ is truly derived.

## 9. Micro-drills

1. Eigenpairs of $\begin{pmatrix}3&1\\1&3\end{pmatrix}$.
   *Ans.* $\lambda=4$ with $(1,1)$; $\lambda=2$ with $(1,-1)$.
2. Is $\begin{pmatrix}1&2\\2&1\end{pmatrix}$ PSD? *Ans.* No: eigenvalues $3,-1$.
3. Sum of the eigenvalues of a $3\times3$ matrix with trace $7$. *Ans.* $7$.
4. Why is $\operatorname{Var}(\sum v_iX_i)\ge0$ relevant to matrices? *Ans.* It proves
   $\Sigma$ is PSD, i.e. it can arise as a covariance.

## 10. Where each idea is used

| Idea | Where |
|---|---|
| $Av=\lambda v$, characteristic equation | Exercises 23, 26 (small explicit eigenproblems) |
| spectral theorem, orthonormal basis | Exercise 20 (orthogonal eigenfunctions) |
| PSD $\iff$ eigenvalues $\ge0$ | Exercise 20 (nonnegative operator) |
| $\operatorname{tr}A=\sum\lambda_i$ | Exercise 22 ($\sum\lambda_n=\int R(t,t)dt$) |
| completion of the square | file 01 §6, deriving $\mathbb Ee^{i\theta X}$ |
| Cholesky $LL^\top$, simulate $L\zeta$ | Exercise 27, `1_4.py`-style sampling |
| rank-one structure $f(t)f(s)$ | Exercises 23, 26 |

**The one line to remember from this file:** *a covariance matrix is nothing but a
PSD matrix, and a PSD matrix is nothing but "a matrix of variances of linear
combinations".* Everything you do with $\Sigma$ is an instance of
$\operatorname{Var}(\sum_iv_iX_i)=v^\top\Sigma v\ge0$.
