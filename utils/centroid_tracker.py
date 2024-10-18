from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np

class CentroidTracker:
    def __init__(self, maxDisappeared=10, maxDistance=50):
        self.nextObjectID = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()
        self.maxDisappeared = maxDisappeared
        self.maxDistance = maxDistance

    def register(self, centroid, shape):
        self.objects[self.nextObjectID] = (centroid, shape)
        self.disappeared[self.nextObjectID] = 0
        self.nextObjectID += 1

    def deregister(self, objectID):
        del self.objects[objectID]
        del self.disappeared[objectID]

    def update(self, detections):
        if len(detections) == 0:
            for objectID in list(self.disappeared.keys()):
                self.disappeared[objectID] += 1
                if self.disappeared[objectID] > self.maxDisappeared:
                    self.deregister(objectID)
            return self.objects
        inputCentroids = np.zeros((len(detections), 2), dtype="int")
        inputShapes = []
        for (i, (centroid, shape)) in enumerate(detections):
            inputCentroids[i] = centroid
            inputShapes.append(shape)
        if len(self.objects) == 0:
            for i in range(len(inputCentroids)):
                self.register(inputCentroids[i], inputShapes[i])
        else:
            objectIDs = list(self.objects.keys())
            objectCentroids = [self.objects[objectID][0] for objectID in objectIDs]
            D = dist.cdist(np.array(objectCentroids), inputCentroids)
            rows = D.min(axis=1).argsort()
            cols = D.argmin(axis=1)[rows]
            assignedRows = set()
            assignedCols = set()
            for (row, col) in zip(rows, cols):
                if row in assignedRows or col in assignedCols:
                    continue
                if D[row, col] > self.maxDistance:
                    continue
                objectID = objectIDs[row]
                self.objects[objectID] = (inputCentroids[col], inputShapes[col])
                self.disappeared[objectID] = 0
                assignedRows.add(row)
                assignedCols.add(col)
            unusedRows = set(range(0, D.shape[0])).difference(assignedRows)
            unusedCols = set(range(0, D.shape[1])).difference(assignedCols)
            if D.shape[0] >= D.shape[1]:
                for row in unusedRows:
                    objectID = objectIDs[row]
                    self.disappeared[objectID] += 1
                    if self.disappeared[objectID] > self.maxDisappeared:
                        self.deregister(objectID)
            else:
                for col in unusedCols:
                    self.register(inputCentroids[col], inputShapes[col])
        return self.objects
