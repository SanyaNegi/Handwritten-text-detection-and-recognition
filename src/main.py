from __future__ import division
from __future__ import print_function


import argparse
import cv2
from DataLoader import Batch
from Model import Model, DecoderType
from SamplePreprocessor import preprocess


class FilePaths:
    "filenames and paths to data"
    fnCharList = '../model/charList.txt'
    fnAccuracy = '../model/accuracy.txt'
    fnTrain = '../data/'
    fnInfer = '../data/roi.png'
    fnCorpus = '../data/corpus.txt'


def infer(model, fnImg,i):
    "recognize text in image provided by file path"
    img = preprocess(cv2.imread(fnImg, cv2.IMREAD_GRAYSCALE), Model.imgSize)
    batch = Batch(None, [img])
    (recognized, probability) = model.inferBatch(batch, True)
    
   
    path="TextFiles/file%s.txt" %i
    with open(path, "a") as file_object:
        file_object.write((recognized[0] + ' '))

    print('Probability:', probability[0])
    

def main():
    "main function"
    # optional command line args
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', help='train the NN', action='store_true')
    parser.add_argument(
        '--validate', help='validate the NN', action='store_true')
    parser.add_argument(
        '--beamsearch', help='use beam search instead of best path decoding', action='store_true')
    parser.add_argument(
        '--wordbeamsearch', help='use word beam search instead of best path decoding', action='store_true')
    parser.add_argument(
        '--dump', help='dump output of NN to CSV file(s)', action='store_true')
    parser.add_argument(
            '--i', help='file number',)

    args = parser.parse_args()

    decoderType = DecoderType.BestPath
    if args.beamsearch:
        decoderType = DecoderType.BeamSearch
    elif args.wordbeamsearch:
        decoderType = DecoderType.WordBeamSearch


    # infer text on images
   
    print(open(FilePaths.fnAccuracy).read())
    model = Model(open(FilePaths.fnCharList).read(),
                      decoderType, mustRestore=True, dump=args.dump)
    infer(model, FilePaths.fnInfer,args.i)


if __name__ == '__main__':
    main()
