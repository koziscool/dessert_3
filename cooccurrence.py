
import sys

def get_words( filename ):
    f = open(filename)
    raw_words = f.read().split()
    words = [ word.lower().strip(".,;:?!'") for word in raw_words]
    return words

def preprocess( words, k ):
    neighbors = {}
    counts = {}

    for word_index, word in enumerate( words ):
        current_neighbors = set()

        if word not in neighbors:
            neighbors[word] = {}

        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

        for i in xrange( word_index - k, word_index + k + 1):
            if i in xrange( len(words) ):
                neighbor_word = words[i]
                if neighbor_word not in current_neighbors and i != word_index:
                    if neighbor_word in neighbors[word]:
                        neighbors[word][neighbor_word] += 1
                    else:
                        neighbors[word][neighbor_word] = 1
                    current_neighbors.add( neighbor_word )

    return neighbors, counts

def cooccurrence( anchor_word, compare_word, neighbors, counts ):
    if anchor_word not in counts:
        return 0

    return neighbors[anchor_word][compare_word] / float( counts[anchor_word] )


if __name__ == '__main__':
    words = get_words( sys.argv[1] )
    neighbors, counts = preprocess( words, int( sys.argv[2] ) )

    while True:
        my_input = raw_input( "Enter 2 words or q to quit: ").split()
        if my_input[0] == 'q':
            break

        print "%.2f" % cooccurrence( my_input[0], my_input[1], neighbors, counts )

