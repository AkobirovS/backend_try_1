import random
from django.shortcuts import render
from rest_framework import serializers
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseNotFound

class WordsSerializator(serializers.ModelSerializer):
    class Meta:
        model = models.Words
        fields = ['pk','word','gender']


class RandomWord(APIView):
    def get(self, *args, **kwargs):
        all_words = models.Words.objects.all()
        random_word = random.choice(all_words)
        serializer_random_word = WordsSerializator(random_word, many=False)
        return Response(serializer_random_word.data)


class NextWord(APIView):
    def get(self, request , pk , format=None):
        word = models.Words.objects.filter(pk__gt=pk).first()
        if not word:
            return HttpResponseNotFound()
        ser_word = WordsSerializator(word, many=False)
        return Response(ser_word.data)

