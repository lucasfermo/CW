import math,os, sys,random,time,turtle,operator
import datetime

#Smallest possible sum

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection=collection
        self.items_per_page=items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)


    # returns the number of pages
    def page_count(self):
        return (len(self.collection)//self.items_per_page)+1

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self,page_index):
        if page_index>self.page_count()-1:
            return -1
        if self.items_per_page*(page_index+1)<len(self.collection):
            return self.items_per_page
        else:
            return len(self.collection)%self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self,item_index):
        if item_index>len(self.collection)-1 or item_index<0:
            return -1
        return item_index//self.items_per_page

collection = range(1,25)
helper = PaginationHelper(collection, 10)

print(helper.item_count())
