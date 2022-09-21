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
X_o = 
\begin{bmatrix} 
rcos(\phi(t)) \\
rsin(\phi(t))
\end{bmatrix}
$$
