# LAAC data analysis tutorial

 * Presenters: Sarah Caudill (physarah (at) g + mail , com)

## Preliminaries

What do data analysts do?
 * We search data for gravitational wave signals.
 * We do astrophysics with the results of the search.
  * If there is a detection, we uncover the physics of the source.
  * If there is no detection, we make a statement about the rate or strength of the gravitational waves.

More specifically,
 * search for continuous gravitational waves from pulsars
 * place upper limits on strength of pulsars' gravitational wave emission
 * search for persistent gravitational waves from extended sources
 * search for gravitational waves associated with pulsar timing glitches
 * search for inspiral, merger, and ringdown gravitational waves associated with coalescing binary black holes
 * place upper limits on a cosmological or astrophysical stochastic background of gravitational waves
 * search for gravitational waves from coalescing compact binary neutron star systems (spinning and non-spinning)
 * place upper limits on rates of inspiral events from binary neutron stars
 * search for gravitational waves from merging intermediate mass black holes
 * place upper limits on rates of merging intermediate mass black holes
 * search for gravitational waves from perturbed intermediate mass black holes
 * search for gravitational wave bursts from cosmic string cusps
 * search for gravitational wave bursts from stellar collapses, mergers of compact binary star systems, and other unmodeled energetic phenomena
 * search for gravitational wave bursts associated with long gamma ray bursts
 * search for gravitational wave bursts associated with high energy neutrinos
 * develop methods for low latency gravitational wave detection
 * develop methods to promptly identify and localize gravitational wave events and request images of targeted sky locations
 * model localization capabilities of advanced detector networks
 * model anticipated gravitational waveforms and test our ability to detect them
 * use Bayesian parameter estimation to determine unknown parameters of waveforms
 * utilize machine learning to classify gravitational wave candidates and detector glitches
 * collaborate with the numerical relativity community to perform studies using recent simulations
 * develop methods to estimate the background in the searches
 * develop new statistics to improve our ability to separate signal from noise
 * develop methods to optimize algorithms
 * ....and lots more

Have you successfully installed all the code? You can check in the following ways:

 * What [Python](https://www.python.org) do you have? It should be version 2.6.x - 2.7.x. In your terminal, type:
```
$ python --version
Python 2.7.1
```
 * Do you have the basic packages for mathematical and scientific computing? These are [Numpy](http://www.numpy.org), [Scipy](http://www.scipy.org), and [matplotlib](http://matplotlib.org). What versions do you have? It should be Numpy >= 1.4, Scipy >= 0.7, and matplotlib >= 0.99. In your terminal, open an ipython session and check the versions:
```

## A Toy Matched Filtering Problem
