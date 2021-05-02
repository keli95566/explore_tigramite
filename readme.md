## Goal

This project explores the possiblity of [tigramite](https://github.com/jakobrunge/tigramite) with different real-world dataset. It is in preparation of a user study that aim for improving the visualization of time series causal graph of tigramite.

## Project Structure

```
├── src
│   ├── model     <- code of building prediction models.
│   ├── data      <- code for post-processing and pre-processing of raws dataset.
│   └── visualize <- source of visualization code.
│ 
├── data
│   ├── raw       <-raw data in the format of csv, etc.
│   │               (If an API to the source is avaliable commit the link.)
│   └── processed  <- processed data in the format of npz 
│                (The npz file can directly be put into tigramite dataframe)
│ 
├── model         <- built models based on tigramite for faster loading.
└── notebook      <- a collection of notebooks documenting experiments on different datasets. 
```
Note:

Keep a clean format of the notebook: ind-initial-name. Example: (01-kl-covid19-epi-exploration)
  * notebook structure:
    * title and experiment descriptions.
    * data processing (loading data from Google drive, convert data to numpy format, etc).
    * causality analysis using Tigramite.
    * user study notes or verbal analysis.



## Resources in Learning More About Tigramite

- Conceptual Introduction
  
  * [Causal Inference and Causal Discovery in Climate Science]((https://www.youtube.com/watch?v=CRrDqhA27gY)) by Marlene Kretschmer, on Mar 2021: This talk gives a basic introduction to the difference of causal inference, causal discovery, and how to do correlation test, and independence test.
  * [Causal inference in Earth system sciences](https://www.youtube.com/watch?v=wJ_AkNELm6Q) by Jakob Runge, on April 2021: This talk gives a comprehensive overview of causal inference and an introduction to time series causal discovery. 
  * [Introducing Environmental Data Science: a new Open Access journal](https://www.youtube.com/watch?v=4pmQ9rGPLWg) Launch event at NeurIPS 2020, how are AI and data science enhancing our understanding of the environment, including climate change?

  
- Algorithm Introduction:
  
  * [ Causal discovery in time series with unobserved confounders](https://www.youtube.com/watch?v=wHipPamwWr0) by Andreas Gerhardus (DLR Jena), on April 8, 2021: This talk gives a shorter overview of causal inference, and an introduction to Latent PCMCI algorithm.

  * [Discovering contemporaneous and lagged causal relations in autocorrelated nonlinear time series](https://www.youtube.com/watch?v=B6SfuOaBFDs) by Jakob Runge, on Oct 2020: This talk gives a brief introduction to the PCMIC+ Algorithm.