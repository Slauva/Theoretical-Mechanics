# Homework third week

## Task 1

![img.png](assets/task1.png)

### Simulation

[Geogebra link](https://www.geogebra.org/m/xnprbgq6)

### Solution

From the given data we need eq-n of the arc length $OM = s_r(t) = 6\pi*t^2$ and transform this to angle eq-n:

$$
\theta(t)=
\begin{cases}
-\frac{s_r(t)}{R} & 0 >= sin(\phi(t)) \\
\frac{s_r(t)}{R} & overwise
\end{cases}
$$

Now, we can calculate angular velocities and accelerations for $\phi(t)$ and $\theta(t)$:

$$
w_o(t) = \dot\phi = \frac{\pi * t^2}{2} \to \overrightarrow{w_o} = (0, 0, \pi * t^2 / 2)
$$

$$
\varepsilon_o(t)=\ddot\phi = \pi * t \to \overrightarrow{\varepsilon_o} = (0,0,\pi * t)
$$

$$
w_m(t) = \dot\theta = \frac{12\pi * t}{R} \to \overrightarrow{w_m} = (0, 0, \frac{12\pi * t}{R})
$$

$$
\varepsilon_m(t)=\ddot\theta = \frac{12\pi}{R} \to \overrightarrow{\varepsilon_m} = (0,0,\frac{12\pi}{R})
$$

Now, lets find the coordinates of points:

$$
r = O_1O = O_2A
$$

$$
X_O =
\begin{bmatrix}
rcos(\phi(t)) \\
rsin(\phi(t))
\end{bmatrix}
$$

$$
X_A = X_O +
\begin{bmatrix}
2R \\
0
\end{bmatrix}
$$

Point $N$ is a center of the circle $D$

$$
X_N = X_O +
\begin{bmatrix}
R \\
0
\end{bmatrix}
$$

$$
X_M = X_N +
\begin{bmatrix}
Rcos(\theta(t)) \\
Rsin(\theta(t))
\end{bmatrix}
$$

After that, lets find the absolute, transport, and relative velocity and acceleration for point $M$

$$
\underline{\underline{\overrightarrow{v^{tr}_M} = w_D*O_1M+\overrightarrow{v_D}=|| w_D=0 ||=\overrightarrow{v_D} =
\overrightarrow{w_o} \times \overrightarrow{r}}}
$$

$$
\underline{\underline{\overrightarrow{v^{rel}_M} = \overrightarrow{w_m} \times \overrightarrow{R}}}
$$

$$
\underline{\underline{\overrightarrow{v_M} = \overrightarrow{v^{tr}_M} + \overrightarrow{v^{rel}_M}}}
$$

Accelerations:

$$
\underline{\underline{{{\overrightarrow{a^{tr}_M} = \overrightarrow{\varepsilon_o} \times \overrightarrow{r} +
\overrightarrow{w_o} \times (\overrightarrow{w_o} \times \overrightarrow{r})}}}}
$$

$$
\underline{\underline{\overrightarrow{a^{rel}_M} = \overrightarrow{\varepsilon_m} \times \overrightarrow{R} +
\overrightarrow{w_m} \times (\overrightarrow{w_m} \times \overrightarrow{R})}}
$$

$$
\underline{\underline{\overrightarrow{a_M} = \overrightarrow{a^{rel}_M} + \overrightarrow{a^{tr}_M} +
\overrightarrow{a^{cor}_M} = ||\overrightarrow{a^{cor}_M} = 0|| = \overrightarrow{a^{rel}_M} + \overrightarrow{a^{tr}_
M}}}
$$

Lets calculate $t$ when $M$ reaches $O$ point:

$$
\theta(t)=2\pi * k \text{, where } k\in Z
$$

$$
\underline{\underline{t = \sqrt{6k}}} \text{, where } k\in Z
$$

## Task 2

![img.png](assets/task2.png)

### Simulation

[Geogebra link](https://www.geogebra.org/m/gekqbyse)

### Solution

From the given data we need eq-n of the arc length $OM = s_r(t) = 75\pi * (0.1t+0.3t^2)$ and transform this to angle eq-n:

$$
\theta(t)= \frac{s_r(t)}{R}
$$

Now, we can calculate angular velocities and accelerations for $\phi(t)$ and $\theta(t)$:

$$
w_D(t) = \dot\phi = 2-0.6t \to \overrightarrow{w_D} = (0, 0, 2-0.6t)
$$

$$
\varepsilon_D(t)=\ddot\phi = -0.6 \to \overrightarrow{\varepsilon_D} = (0,0,-0.6)
$$

$$
w_m(t) = \dot\theta = \frac{75\pi * (0.1+0.6t)}{R} \to \overrightarrow{w_m} = (0, 0, \frac{75\pi * (0.1+0.6t)}{R})
$$

$$
\varepsilon_m(t)=\ddot\theta = \frac{75\pi * 0.6}{R} \to \overrightarrow{\varepsilon_m} = (0,0,\frac{75\pi * 0.6}{R})
$$

Now, lets find the coordinates of points:

$$
X_O = 
\begin{bmatrix} 
Rcos(\phi(t)) \\
Rsin(\phi(t))
\end{bmatrix}
$$

$$
X_M = X_O +
\begin{bmatrix} 
Rcos(\theta(t)) \\
Rsin(\theta(t))
\end{bmatrix}
$$

Point $N$ is a center of the circle $D$

After that, lets find the absolute, transport, and relative velocity and acceleration for point $M$:

$$
\underline{\underline{\overrightarrow{v^{tr}_M} = w_D*O_1M+\overrightarrow{v_D}=|| v_D=0 || = \overrightarrow{w_D} \times \overrightarrow{O_1M}}}
$$

$$
\underline{\underline{\overrightarrow{v^{rel}_M} = \overrightarrow{w_m} \times \overrightarrow{R}}}
$$

$$
\underline{\underline{\overrightarrow{v_M} = \overrightarrow{v^{tr}_M} + \overrightarrow{v^{rel}_M}}}
$$

Accelerations:

$$
\underline{\underline{{{\overrightarrow{a^{tr}_M} = \overrightarrow{\varepsilon_D} \times \overrightarrow{O_1M} + \overrightarrow{w_D} \times (\overrightarrow{w_D} \times \overrightarrow{O_1M})}}}}
$$

$$
\underline{\underline{\overrightarrow{a^{rel}_M} = \overrightarrow{\varepsilon_m} \times \overrightarrow{R} + \overrightarrow{w_m} \times (\overrightarrow{w_m} \times \overrightarrow{R})}}
$$

$$
\underline{\underline{\overrightarrow{a^{cor}_M} = \overrightarrow{w_D} \times \overrightarrow{v_M}}}
$$

$$
\underline{\underline{\overrightarrow{a_M} = \overrightarrow{a^{rel}_M} + \overrightarrow{a^{tr}_M} + \overrightarrow{a^{cor}_M}}}
$$

Lets calculate $t$ when $M$ reaches $O$ point:

$$
\theta(t)=2\pi * k \text{, where } k\in Z
$$

$$
\underline{\underline{t = \frac{1}{6}(\sqrt{96k+1}-1)}} \text{, where } k\in Z
$$