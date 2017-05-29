word_count_in_test = {}

with open('test.txt') as test_file:
    for line in test_file:
        words = line.strip().split(' ')
        for word in words:
            word = ''.join(l for l in word if l not in ('?', '.', ','))
            word_count_in_test[word] = word_count_in_test.get(word, 0) + 1

    for word, number in word_count_in_test.items():
        print "{} {}".format(word, number)

# word_count_in_test = {}

# with open('twain.txt') as test_file:
#     for line in test_file:
#         words = line.strip().split(' ')
#         for word in words:
#             word = ''.join(l for l in word if l not in ('?', '.', ','))
#             if word not in word_count_in_test:
#                 word_count_in_test[word] = word_count_in_test.get(word, 0) + 1
#             else:
#                 word_count_in_test[word] += 1
#     for word, number in word_count_in_test.iteritems():
#         print "{} {}".format(word, number)
