import hashlib
import multiprocessing


def search(key, start, step, target, resultQueue):
    prefix = "0" * target
    baseHash = hashlib.md5(key.encode())
    count = start
    
    while True:
        candidateHash = baseHash.copy()
        candidateHash.update(str(count).encode())
        
        if candidateHash.hexdigest()[:target] == prefix:
            resultQueue.put(count)
            return
        count += step

def findHash(key, target):
    resultQueue = multiprocessing.Queue()
    numWorkers = multiprocessing.cpu_count() // 2
    processes = [
        multiprocessing.Process(target=search, args=(key, i, numWorkers, target, resultQueue))
        for i in range(numWorkers)
    ]
    
    for p in processes: p.start()
    result = resultQueue.get()
    for p in processes: p.terminate()
    
    return result

if __name__ == "__main__":
    with open("input.txt") as f:
        key = f.read().strip()

    print(findHash(key, 5))
    print(findHash(key, 6))