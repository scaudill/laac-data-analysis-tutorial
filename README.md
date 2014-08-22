# LAAC data analysis tutorial

 * Presenters: Sarah Caudill (physarah@gmail.com), Alex Urban

## Preliminaries

What do data analysts do?
 * We search data for gravitational wave signals.
 * We do astrophysics with the results of the search.
  * If there is a detection, we uncover the physics of the source.
  * If there is no detection, we make a statement about the rate or strength of the gravitational waves.

More specifically,
 * We search for
  * gravitational waves from coalescing compact binary neutron star systems (spinning and non-spinning)
  * inspiral, merger, and ringdown gravitational waves associated with coalescing binary black holes
  * continuous gravitational waves from pulsars
  * gravitational wave bursts from stellar collapses, mergers of compact binary star systems, and other unmodeled energetic phenomena
  * gravitational wave bursts associated with long gamma ray bursts
  * gravitational wave bursts associated with high energy neutrinos
  * persistent gravitational waves from extended sources
  * gravitational waves associated with pulsar timing glitches
  * gravitational waves from merging intermediate mass black holes
  * gravitational waves from perturbed intermediate mass black holes
  * gravitational wave bursts from cosmic string cusps
 * We place upper limits on
  * strength of pulsars' gravitational wave emission
  * cosmological or astrophysical stochastic background of gravitational waves
  * rates of inspiral events from binary neutron stars
  * rates of merging intermediate mass black holes
 * We develop methods
  * for low latency gravitational wave detection
  * to promptly identify and localize gravitational wave events and request images of targeted sky locations
  * to estimate the background in the searches
  * to optimize algorithms
 * model localization capabilities of advanced detector networks
 * model anticipated gravitational waveforms and test our ability to detect them
 * use Bayesian parameter estimation to determine unknown parameters of waveforms
 * utilize machine learning to classify gravitational wave candidates and detector glitches
 * collaborate with the numerical relativity community to perform studies using recent simulations
 * develop new statistics to improve our ability to separate signal from noise
 * ....and lots more

## A Toy Matched Filtering Problem

There is a simple matched filtering toy code called matched_filter.py in this repository. In order to run it, you will need python, numpy, and matplotlib as well as the data and utilities in this repository. This example was adapted from Mike Boyle's MatchedFiltering code available from his github repository (https://github.com/moble/MatchedFiltering).

To check out this repository, do
```
git clone https://github.com/scaudill/laac-data-analysis-tutorial.git
```

The matched_filter.py code can be run by simply doing
```
python matched_filter.py
```

Starting on Line 10 of the code, you can change the following parameters to make different signals and templates:
```
# Set your favorite parameters
SamplingFrequency = 8192.0
DistanceInMegaparsecs = 10.0
SignalMassInSolarMasses = 5.0
TemplateMassInSolarMasses = 5.0
```
