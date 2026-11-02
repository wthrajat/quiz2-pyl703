# Curie–Weiss temperature and magnetic order

The Curie–Weiss intercept describes the response to a uniform magnetic field. An ordering temperature marks the onset of a particular spin pattern. Their signs and relative sizes provide clues, but they need not measure the same combination of interactions.

## Two different interaction scales

For equivalent spins in an isotropic exchange model, take positive exchange to mean ferromagnetic coupling. The uniform intercept is proportional to the sum of the exchanges, whereas the mean-field ordering temperature follows the strongest ordering mode. Exchanges can cancel in the uniform sum while reinforcing a different spatial pattern.

For example, let x be the total ferromagnetic coupling within a layer and y the magnitude of antiferromagnetic coupling between layers. The uniform intercept is proportional to x − y, while the alternating-layer instability is proportional to x + y. This illustrates a mechanism; it does not fit exchange constants to an experimental material.

MnBi2Te4 provides a physical layered example: ferromagnetic Mn layers couple antiparallel. Its reported ordering temperature is 24.2 K, but the fitted intercept is only 3 ± 3 K. The uncertainty and sensitivity to the fitted background mean that its positive sign is not secure. Directional magnetization, magnetic circular dichroism, and exchange calculations establish the arrangement more directly. [2]

## Numerical examples

The table is generated from the literature examples in `data/materials.csv`. All temperatures are in kelvin. Values marked as magnitudes have no signed intercept assigned in this dataset.

| Material / structure | Intercept (K) | Ordering (K) | Ratio |
|---|---:|---:|---:|
| YMnO3 / hexagonal | -417 | 71 | 5.873 |
| LuMnO3 / hexagonal | -519 | 90 | 5.767 |
| ScMnO3 / hexagonal | -495 | 130 | 3.808 |
| YMnO3 / orthorhombic | -26 | 42 | 0.619 |
| MnBi2Te4 / rhombohedral | 3 ± 3 | 24.2 | 0.124 |
| GdMnO3 / orthorhombic | -39 | — | — |
| YCrO3 / orthorhombic | |theta| = 260 | 140 | 1.857 |
| LuCrO3 / orthorhombic | |theta| = 129 | 115 | 1.122 |
| HoCrO3 / orthorhombic | |theta| = 19 | 142 | 0.134 |

## A small intercept does not imply weak interactions

In the same hydrothermal orthochromite study, YCrO3 and HoCrO3 order at 140 and 142 K, although their reported intercept magnitudes are 260 and 19 K. The source gives these as absolute values, which are preserved as such here. Their ratios are about 1.86 and 0.134. [5]

The rare-earth ion in HoCrO3 adds a large magnetic response to that of chromium. In an illustrative limit, add an independent rare-earth Curie susceptibility to a chromium Curie–Weiss susceptibility. Expanding at high temperature gives an effective intercept equal to the chromium intercept multiplied by C_Cr / (C_Cr + C_R), where the C values are the respective Curie constants. The bulk intercept can shrink without reducing the chromium ordering scale. Rare-earth–chromium exchange and crystal-field effects complicate this simple limit.

## Large ratios and the evidence for frustration

Hexagonal YMnO3, LuMnO3, and ScMnO3 have ratios of about 5.87, 5.77, and 3.81. Their triangular Mn lattices support a frustration interpretation: antiferromagnetic interactions cannot satisfy every bond simultaneously. All three nevertheless have established ordered phases. A large ratio alone does not establish a glass, a spin liquid, or a unique spin geometry. [1]

The same paper reports susceptibility measurements up to 400 K and fits over 300–400 K. This interval is above the ordering transitions but not well above the intercept magnitudes. The paper explicitly warns that the fitting interval is too low. These are faithfully reported fit parameters, rather than exact asymptotic exchange scales. [1]

## Check the denominator and the source column

For orthorhombic YMnO3, the reported pair gives 26 / 42 = 0.619. The sign and ratio do not reveal its sinusoidally modulated spin structure; diffraction provides that information. [3]

For GdMnO3, 2 K is the temperature of a magnetization-loop measurement, not an established ordering transition in the cited experiment. Dividing 39 by 2 would produce a number with an unsupported physical denominator, so this dataset leaves its ordering temperature and ratio blank. [4]

The orthochromite table also distinguishes the current study's measurements from adjacent historical values. This dataset uses the current study's magnitudes: 260 K for YCrO3, 129 K for LuCrO3, and 19 K for HoCrO3. It neither silently substitutes the historical values nor infers a sign from an absolute-value heading. [5]

## References

[1] [The magnetic susceptibility, specific heat and dielectric constant of hexagonal YMnO3, LuMnO3 and ScMnO3](https://arxiv.org/pdf/cond-mat/0103609). Journal of Physics: Condensed Matter 13, 4543 (2001). Table I and susceptibility section.

[2] [Prediction and observation of an antiferromagnetic topological insulator](https://arxiv.org/pdf/1809.07389). Nature 576, 416–422 (2019). Magnetic measurements and Figure 2.

[3] [The magnetic structure of YMnO3 perovskite revisited](https://doi.org/10.1088/0953-8984/14/12/315). Journal of Physics: Condensed Matter 14, 3285–3294 (2002). Magnetic measurements and neutron-diffraction sections.

[4] [Structural, Optical and Magnetic Properties of Multiferroic GdMnO3 Nanoparticles](https://doi.org/10.1007/s10948-012-1870-0). Journal of Superconductivity and Novel Magnetism 26, 1611–1615 (2013). Magnetic-properties section and Figure 6.

[5] [Direct Hydrothermal Synthesis and Physical Properties of Rare-Earth and Yttrium Orthochromite Perovskites](https://doi.org/10.1021/cm102925z). Chemistry of Materials 23, 48–56 (2011). Table 3, own-sample columns; magnetic-properties discussion.
