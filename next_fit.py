# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:25:14 2021

@author: hp
"""

def next_fit (block_size,total_blocks,process_size,total_process):
    allocation = []
    allocation = [-1] * total_process
    j = 0
    for i in range(total_process):
        while j < total_blocks:
            if block_size[i] >= process_size[i]:
                allocation[i] = j
                block_size[j] -= process_size[i]
                break
            
            j = (j + 1)% total_blocks
            
    print("Process No. Process Size Block no.")
    for i in range(total_process):
        print(" ", i + 1, "   ", process_size[i], " ", end = " ") 
        if allocation[i] != -1: 
            print(allocation[i] + 1) 
        else:
            print("Not Allocated")
            
blockSize = [5, 10, 20] 
processSize = [10, 20, 5]
x = len(blockSize) 
y = len(processSize) 
next_fit(blockSize, x, processSize, y)