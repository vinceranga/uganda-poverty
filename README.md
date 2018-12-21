## Mapping Poverty in Uganda through Object Detection on Satellite Imagery

Vince Ranganathan, Stanford University

Stanford Sustainability & Artificial Intelligence Lab

Under mentorship of Neal Jean, Stefano Ermon, and Marshall Burke.

July 2018 - now; updated 12/21/2018


Operating up-to-date object detection models on high-resolution satellite imagery to identify indicators of poverty and economic inequality within Uganda. The target of this project is to use machine learning models to extract metrics such as distributions of house size, house density over the area, house material, car size, car density over the area ... and identify subtle links between metrics that are indicators of poverty. These relations are then used to predict levels of poverty within subregions in Uganda.

_Why is it important to analyze these metrics? How does the correlation between density of houses and density of cars matter?_ Consider a region that is primarily a slum. It will have a high density of houses, small average house size, lack of water bodies or green regions, and low density of cars (which typically do not fit inside slums). Additionally, the most overwhelming color will match the roofing style, which is typically grey aluminum sheets. The model will connect these variables to predict that the region is a slum, and thus have a high density of people but a low average income. This is more evident example, but a machine learning model will be able to pick up on subtelties that may be of significant use to policy-makers and international aid efforts.

Informal poster available at: https://drive.google.com/file/d/1UOCmL-kd8EUbzdqqdAYX16QGOyzbMIEH/view?usp=sharing

![alt text](https://github.com/vinceranga/uganda-poverty-project/blob/master/poster/uganda-survey.png "Uganda Map")

![alt_text](https://github.com/vinceranga/uganda-poverty-project/blob/master/test-out/dg_lsms_uganda_1000x1000_21430002_479_tops5x5-1.jpeg "Object detection")

This work is inspired by Jean et al.'s research on nighttime lighting to predict poverty: http://science.sciencemag.org/content/353/6301/790

These scripts are typically run on an instance on the Google Cloud Platform.

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
- extracting metrics from this data, e.g.:
  - number of houses
  - the density of houses within these clusters
  - distribution of cluster size
  - distribution of house size, both in the region and within clusters

Future work will entail expanding the object detection model from just buildings to other indicators, such as cars, roads, farms, and water bodies. A neural network will be developed to make some sense of which metrics are relevant, and how these relate to each other.

-----------------------------------------------------------------------------------------------------------------------

utils.py contains utility functions for the YOLOv3 object detection model.

hyper.py contains hyperparameters, and is accessed by all of the Jupyter Notebooks.

The weights for the YOLO model are too heavy to be uploaded here. (Unlike the weights I lift at the gym :/)
