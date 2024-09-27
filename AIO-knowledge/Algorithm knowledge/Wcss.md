#Algorithm #Math #Loss

# WCSS in K-Means

**WCSS (Within-Cluster Sum of Squares)** in the **K-Means** algorithm is a metric used to evaluate the compactness of data points within a cluster relative to the cluster centroid. It represents the total squared distance between each data point in a cluster and the centroid of that cluster.

Specifically, WCSS is calculated by summing the squared Euclidean distances between each data point and the centroid of the cluster it belongs to. The goal of the K-Means algorithm is to minimize WCSS, meaning that it tries to make data points in each cluster as close to their respective centroid as possible, thereby making the clusters more "compact."

The formula for WCSS for a cluster is as follows:

\[
WCSS = \sum_{x \in C} (x - \mu)^2
\]

Where:
- \( x \) is a data point in cluster \( C \),
- \( \mu \) is the centroid (mean of the points in the cluster),
- \( (x - \mu)^2 \) is the squared distance between \( x \) and \( \mu \).

## Meaning of WCSS:
- The smaller the WCSS, the closer the data points in the cluster are to each other, indicating a "tighter" cluster.
- In the K-Means algorithm, the **Elbow Method** is often used to choose the optimal number of clusters (k) based on the WCSS plot. As the number of clusters increases, WCSS decreases, but beyond a certain point, the decrease in WCSS becomes less significant. This point is called the "elbow" and is considered the optimal number of clusters.

Hope this helps you better understand WCSS in K-Means!