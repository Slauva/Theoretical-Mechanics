## Week 7 homework

### Simulation

### Task

![img.png](assets/task1.png)

> RO:
> 1. particle (reactlinear motion)
> 2. rigid body (rectlinear motion)
> 3. homogeneous disk (rotation)
>
> Method: Euler-Lagrange
>
> Force analysis:
> 
> $G_1 = m_1 * g = 10$, $G_2 = m_2 * g = 30$, $G_3 = m_3 * g = 20$
> 
> $R = -b * \dot{x}$, $N_1 - ?$, $N_3 - ?$

#### Condition



|   | Initial | Final |
| -------- | -------- | -------- |
| $x$     | 0     | ?     |
| $\dot{x}$    | 0     | ?     |
| $\xi$     | 0     | ?     |
| $\dot{\xi}$     | 3     | ?     |
| $t$     | 0     | ?     |



#### Kinematic analysis:

$v_2 = \dot{x} = v_3 \to v_3 = w_3r \to w_3 = \frac{\dot{x}}{r}$

$v^2_1 = \dot{x}^2 + \dot{\xi}^2 + 2 * \dot{x} * \dot{\xi} * cos(\beta)$

#### Momentum of Inertion

$J_3 = \frac{1}{2} \sum^n_{k=0}{m_kr^2_k} = r^2$

#### Solution

At first, lets calculate the kinematic and potential energy for each body:

$$T_1 = \frac{m_1 * v^2_1}{2} = \frac{\dot{x}^2 + \dot{\xi}^2 + 2\dot{x}\dot{\xi}cos(30^{\circ})}{2}$$

$$T_2 = \frac{m_2 * v^2_2}{2} = \frac{3\dot{x}^2}{2}$$

$$T_3 = \frac{m_3v^2_3}{2} + \frac{J_3w^2_3}{2} = \frac{3\dot{x}^2}{2}$$

$$T = T_1 + T_2 + 2T_3 = \frac{\dot{x}^2 + \dot{\xi}^2 + 2\dot{x}\dot{\xi}cos(30^{\circ})}{2} + \frac{3\dot{x}^2}{2} + 3\dot{x}^2 = 5\dot{x}^2 + (\dot{\xi}^2 + \dot{x}\dot{\xi}\sqrt{3}) * \frac{1}{2}$$

$$\Pi_1 = - G_1(x sin(\alpha) + \xi sin(\alpha + \beta)) = -5 (x + \xi \sqrt{3})$$

$$\Pi_2 = - G_2 x sin(\alpha) = -15x$$

$$\Pi_3 = - G_3 x sin(\alpha) = -10x$$

$$\Pi = \Pi_1 + \Pi_2 + 2 \Pi_3 = -5 (x + \xi \sqrt{3}) - 35x$$
