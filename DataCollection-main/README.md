# DataCollection
## Areas
* Semantic segmentation
* Image classification
* Object detection
* Object Recognition
* Domain adaptation
* Image generation
* Image augmentation
* Pose estimation
* Autonomous vehicles
* Denoising
* Super-Resolution
* Object Tracking
* Action Recognition
* Face Recognition
* Depth Estimation
* Optical Character Recognition
* 3D Reconstruction
* Image Retrieval
* Optical Flow Estimation
* Style Transfer
* Image Compression
* Image Captioning
## Strategies
First generate/write vogue queries for these areas\
Then get papers for each of these areas
## How to get papers
* mannuly selection
* search area on google scholar (400 for each area)
* search area on semantic scholar (200 for each area)
* search area on paperswithcodes (200 for each area)

## Data format
Notice that rating for the retrival results from these resourcesare done in the following way:
* 1: not retrived in this resource, but in other resource
* 2: 200< rank <=400
* 3: 100 < rank <= 200
* 4: 40 < rank <= 100
* 5: rank <= 40
And the aggregate are done as follows:
0.3\*data from google scholar + 0.3\*data from semantic scholar + 0.4*data from paperswithcodesß
### new_test_set.csv
* area
* rank_gs: the rank of the paper in google scholar, if is 401, means the paper is not in google scholar retreived result for top 400
* rank_ss: the rank of the paper in semantic scholar, if is 201, means the paper is not in semantic scholar retreived result for top 200
* rank_pc: the rank of the paper in paperswithcodes, if is 201, means the paper is not in paperswithcodes retreived result for top 200
* rate_gs: the rating of the paper in google scholar, if is 0, means the paper is not in google scholar retreived result for top 400
* rate_ss: the rating of the paper in semantic scholar, if is 0, means the paper is not in semantic scholar retreived result for top 200
* rate_pc: the rating of the paper in paperswithcodes, if is 0, means the paper is not in paperswithcodes retreived result for top 200
* title: the title of the paper
* agg_rate: the rating of the paper aggregated from google scholar, semantic scholar and paperswithcodes
* agg_rank: the rank of the paper aggregated from google scholar, semantic scholar and paperswithcodes
* rank: rank based first on agg_rate, then on agg_rank
* pdf_link: the link to the pdf of the paper
* abstract: the abstract of the paper
* citationCount: the citation count of the paper
* referenceCount: the reference count of the paper
* influentialCitationCount: the influential citation count of the paper
* fieldOfStudy: the very general field of study of the paper
### final_data.csv
* area
* rank_gs: the rank of the paper in google scholar, if is 401, means the paper is not in google scholar retreived result for top 400
* rank_ss: the rank of the paper in semantic scholar, if is 201, means the paper is not in semantic scholar retreived result for top 200
* rank_pc: the rank of the paper in paperswithcodes, if is 201, means the paper is not in paperswithcodes retreived result for top 200
* rate_gs: the rating of the paper in google scholar, if is 0, means the paper is not in google scholar retreived result for top 400
* rate_ss: the rating of the paper in semantic scholar, if is 0, means the paper is not in semantic scholar retreived result for top 200
* rate_pc: the rating of the paper in paperswithcodes, if is 0, means the paper is not in paperswithcodes retreived result for top 200
* title: the title of the paper
* agg_rate: the rating of the paper aggregated from google scholar, semantic scholar and paperswithcodes
* agg_rank: the rank of the paper aggregated from google scholar, semantic scholar and paperswithcodes
* rank: rank based first on agg_rate, then on agg_rank
* pdf_link: the link to the pdf of the paper
* abstract: the abstract of the paper
* citationCount: the citation count of the paper
* referenceCount: the reference count of the paper
* influentialCitationCount: the influential citation count of the paper
* fieldOfStudy: the very general field of study of the paper