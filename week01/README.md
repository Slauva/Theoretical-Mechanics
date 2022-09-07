# Homework first week

## Task 1

![task 1](assets/task1.png)

### Simulation

![simulation 1](assets/task1.gif)

### Solution

We have the system of $x(t)$ and $y(t)$, where $t\in[-5,5]$.

$$
\begin{cases}
x(t)=3t \\
y(t) = 4t^2+1
\end{cases}
$$

Into the task, we need to find the equation $y(x)$ and vectors: $\vec{v}$, $\vec{a}$, $\vec{a_{\tau}}$, $\vec{a_n}$

$$
\begin{cases}
x(t)=3t \\
y(t) = 4t^2+1
\end{cases} \to t=\frac{x}{3} \to \underline{\underline{y(x)=4\frac{x^2}{9}+1}}
$$

$v_x = \dot{x} = 3$

$v_y = \dot{y} = 8t$

$\underline{\underline{\vec{v}}} = v_x \vec{i} + v_y \vec{j} = \underline{\underline{3 \vec{i} + 8t \vec{j}}}$

$a_x = \ddot{x} = 0$

$a_y = \ddot{y} = 8$

$\underline{\underline{\vec{a}}} = a_x \vec{i} + a_y \vec{j} = \underline{\underline{0 \vec{i} + 8 \vec{j}}}$

$$
\underline{\underline{a_{\tau}}} = \frac{a*v}{v} = \underline{\underline{\frac{64t}{\sqrt{9+64t^2}}}}
$$

$$
\underline{\underline{a_n}} = \sqrt{a^2-a_{\tau}^2} = \underline{\underline{\frac{24}{\sqrt{9+64t^2}}}}
$$

$$
\underline{\underline{k}} = \frac{a_n}{v^2} = \underline{\underline{\frac{24}{(9+64t^2)^{\frac{3}{2}}}}}
$$

## Task 2

![task2](assets/task2.png)

### Simulation

[Geogebra visualization](https://www.geogebra.org/m/kpebm7du)

### Solution

From the task we know that $OA = 25$, $AB = 80$, $AC = 20$, $w=const=1$, $\theta = 60$ deg.

All system work into the interval $t\in[0,2\pi]$

In the system we see that $OA$ is a radius of circle $O$, then $OA=R$

* Lets the function $th(t) = \frac{\pi}{2} + wt$ will give us the angle in position of $t$
* At first, we need to find the polar coordinates of point $A$

$$
\begin{cases}
x_a(t) = R*cos(th(t)) \\
y_a(t) = R*sin(th(t))
\end{cases}
$$

* To set the position of point B, we need to find the eq-n for coordinate $y_b(t)$

$$
y_b(t)=- cot(\theta)*x_b(t) + R
$$

* The next, find coordinate $x_b(t)$
* Using the eq-n $y_b(t)$ and Pythagoras' theorem to find distance between $A$ and $B$, we can build the system to
  determine the $x_b(t)$

$$
\begin{cases}
y_b(t)=- cot(\theta)*x_b(t) + R \\
(x_b - x_a)^2 + (y_b - y_a)^2 = AB^2
\end{cases}
$$

* To prettify the formula, let's divide it into the three part

$$
a = 1+cot(\theta)^2
$$

$$
b(t) = R(cot(\theta)*sin(th(t)) -2*cot(\theta)-2*cos(th(t)))
$$

$$
c(t) = R^2-R^2*sin(th(t))-AB^2
$$

$$
x_b(t) = \frac{-b(t) + \sqrt{b(t)^2-4*a*c(t)}}{2*a}
$$

* After that, we can find the velocity and acceleration of $B$

$$
v_b(t)=x_b'(t)\vec{i}+y_b'(t)\vec{j}
$$

$$
a_b(t)=x_b''(t)\vec{i}+y_b''(t)\vec{j}
$$

* To find position of point $C$, firstly we need to determine the path relatively the point $B$

$$
s(t)=\sqrt{(x_a(t)-x_b(t))^2+(y_a(t)-y_b(t))^2}
$$

$$
\begin{cases}
x_c(t)=x_b(t)+(AB-AC)\frac{x_a(t)-x_b(t)}{s(t)} \\
x_c(t)=y_b(t)+(AB-AC)\frac{y_a(t)-y_b(t)}{s(t)}
\end{cases}
$$

* After that, we can find the velocity and acceleration of $C$

$$
v_c(t)=x_c'(t)\vec{i}+y_c'(t)\vec{j}
$$

$$
a_c(t)=x_c''(t)\vec{i}+y_c''(t)\vec{j}
$$

$$
a^{\tau}_c(t)=\frac{a_c(t)*v_c(t)}{v_c(t)*v_c(t)}*v_c(t)
$$

$$
a^{n}_c(t)=a_c(t) - a^{\tau}_c(t)
$$

## Task 3

![img.png](assets/task3.png)

### Solution

