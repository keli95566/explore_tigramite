## Goal

This project explores the possiblity of tigramite with different real-world dataset.

## Project Structure

* src
  * model : source code of building prediction models based on tigramite
  * data: collection of source code using real-world data using pandas, tigramite, etc.
  * visualize: collection of source of visualization code for tigramite.

* data
  * raw: raw data in the format of csv, etc
  * processed: processed data in the format of npz which could directly be used for building tigramite dataframe.

* model: built probablistic models based on tigramite for faster loading.

* notebook: a collection of notebooks which document experiments on different datasets. Keep a clean format of the notebook: ind-initial-name. Example: (01-kl-covid19-epi-exploration)
  * notebook structure:
    * title and experiment descriptions.
    * data processing (loading data from Google drive, convert data to numpy format, etc).
    * causality analysis using Tigramite.
    * user study notes or verbal analysis.