## Mapping Poverty in Uganda through Object Detection on Satellite Imagery

Vince Ranganathan

Stanford Sustainability & Artificial Intelligence Lab

Under mentorship of Neal Jean, Stefano Ermon, and Marshall Burke.

July 2018 - now, updated 12/21/2018


Operating up-to-date object detection models on high-resolution satellite imagery to identify indicators of poverty and economic inequality within Uganda.

Informal poster available at: https://drive.google.com/file/d/1UOCmL-kd8EUbzdqqdAYX16QGOyzbMIEH/view?usp=sharing

The Jupyter Notebooks can be opened in the order they are described below to provide a sense of the flow and check out the visualisations.

-----------------------------------------------------------------------------------------------------------------------

data-info.ipynb visualizes the survey data, displaying:
- (all) the approximate points where the survey was held (after a 5km jitter radius, which was instated to retain anonymity of responders)
- (green) locations that are "urban", an in particular the cluster at Kampala
- (red) locations that are being considered in the sample. This is variable, but is fixed for development purposes.

yolo-250.ipynb runs a YOLOv3 model trained on the xView satellite imagery dataset (updated August 2018, due for update in January 2019):
- draws bounding boxes around each proposed house
- uses a sanity-check to eliminate reasonably incorrect guesses (e.g. boxes of majority green, outside a liberal area range, with funky length/width ratios)
- saves these boxes as a pickle file to be loaded easily into the next notebook

cluster_villages.ipynb considers the 10km x 10km region formed around a survey point, and:
- creates an area graph of the locations of houses, according to the output data from the YOLO object detection model
- opens this region in Google Maps for the human to digress while pretending to be productive
- implements DBSCAN clustering (chosen for its relevant properties, beautifully visualized at https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html) to identify the _k=5_ largest clusters of buildings
- filters out the buildings not a part of these five clusters (denoising)
- begins extracting metrics from this data, e.g. the density of houses within these clusters

-----------------------------------------------------------------------------------------------------------------------

utils.py contains utility functions for the YOLOv3 object detection model.

hyper.py contains hyperparameters, and is accessed by all of the Jupyter Notebooks.

The weights for the YOLO model are too heavy to be uploaded here. (Unlike the weights I lift at the gym :/)
