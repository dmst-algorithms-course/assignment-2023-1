import sys

method = sys.argv[1]
filename = sys.argv[2]
data = []
with open(filename, "r") as f :
    data = [int (x) for x in f.read().split()]

clusters = [[x] for x in data]
clusters.sort()

while(len(clusters)) > 1 :
    min_distance = float('inf')
    closest = None
    
    
    for i in range(len(clusters) - 1) :
        for j in range(i+1 , len(clusters)) :
            l= len(clusters[i])-1
            l2= len(clusters[j])-1
            
            if len(clusters[i]) == 1 and len(clusters[j]) == 1 :
                distance = abs(clusters[i][0] - clusters[j][0])
                
            else :
                if method == "single":
                     distance = 0.5*abs(clusters[i][0]-clusters[j][0]) + 0.5*abs(clusters[i][l]-clusters[j][0])-0.5*(abs(clusters[i][0]-clusters[j][l2]) - abs(clusters[i][l]-clusters[j][l2]))
                elif method == "complete":
                    distance = 0.5*abs(clusters[i][0]-clusters[j][l2]) + 0.5*abs(clusters[i][l]-clusters[j][l2]) + 0.5*(abs(clusters[i][0]-clusters[j][l2]) - abs(clusters[i][l]-clusters[j][l2]))
                    
                elif method == "average" :
                    distance_i = sum([abs(clusters[i][k]-x) for k in range(len(clusters[i])) for x in clusters[j]])/(len(clusters[i]) *len(clusters[j]))
                    distance_j = sum([abs(clusters[j][k]-x) for k in range(len(clusters[j])) for x in clusters[i]])/(len(clusters[i]) *len(clusters[j]))
                    a_i = len(clusters[i]) / (len(clusters[i])+len(clusters[j]))
                    a_j = len(clusters[j]) / (len(clusters[i])+len(clusters[j]))
                    distance = a_i*distance_i + a_j*distance_j
                elif method == "ward":
                        
                    v=clusters[i]+clusters[j]
                    
                    d1=[abs(clusters[i][k]-x) for k in range(len(clusters[i])) for x in clusters[i]]
                    d2=[abs(clusters[j][k]-x) for k in range(len(clusters[j])) for x in clusters[j]]
                    d3=[abs(a-b) for a in clusters[i] for b in clusters[j]]
                    
                    a_i = (len(clusters[i]) +len(v))/ (len(clusters[i])+len(clusters[j])+len(v))

                    a_j = (len(clusters[j]) +len(v))/ (len(clusters[i])+len(clusters[j])+len(v))
                    beta = -len(v)/(len(clusters[i])+len(clusters[j])+len(v))
                    
                    distance = a_i*len(d1) +a_j*len(d2) + beta*len(d3)
                    

            if distance < min_distance :
                min_distance = distance
                closest = (i, j)
    
    if closest :
        i,j = closest
        clusters[i].extend(clusters[j])
        del clusters[j]

    print("({}) {:.2f} {}".format(' '.join(map(str, clusters[i])), min_distance, len(clusters[i])))
