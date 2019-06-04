# pound starts a comment, this line doesn't get run

import os  # os is part of the 'standard library', packages that you can use that you don't have to download
# some packages have to be download first.  search those at https://pypi.org/
# download with 'pip3 install <package_name>'

# get the directory (folder) of this file
current_directory = os.path.dirname(__file__)
# reference the CSV file from this directory so you're never wrong
path_to_in_csv = os.path.join(current_directory, 'in.csv')
path_to_out_csv = os.path.join(current_directory, 'out.csv')

# make sure the file is where you think it is
# the first {} is replaced by the first entry in format()
print('the CSV file is located at {}'.format(path_to_in_csv))


# this is a function.  refernce: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# we just want to get the conversion logic into it's own spot
def convert_size(tire_size):
    # this is the dumbest possible way to do this, mainly because I didn't want to look up tire conversion
    # stuff or put too much energy into this part. We are just replacing one string with another.  This only
    # works if the string is exact.
    if tire_size == '35x12.5 R17':
        return '315/70 R17'
    else:
        # if the tire size doesn't match what we're looking to convert just return what we were given
        return tire_size


# define a list that we can add all of our entries to, so that we can write them later
# the more efficient way to do this is to read from one file, do the operation and then write to the
# other file at the same time, but that's more complex logic than I wanted to give you.
out = []

# open the CSV
# the 'r' mean you're opening it in 'read' mode.  read only, no writing allowed.
# assign the open file to the variable csv_file.
with open(path_to_in_csv, 'r') as csv_file:
    # this is a while loop, which will loop *while* the condition is true.  Since we git it True it will ALWAYS loop.
    while True:
        # read the next line from the file and assign it to the line variable
        line = csv_file.readline()

        # if not line basically checks whether 'line' exists.  This is true if is DOES NOT exist
        if not line:
            # break will break out of our loop.. so the while True
            # if this is true, so the line is not a thing, then we've reached the end of the file and should quit the while loop
            break

        # if the line does exist we will get here and we can do the real stuff

        # define a list to hold each line, right before we add it to the bigger out list
        out_line = []

        # split all entries in the line into a list.  reference: https://docs.python.org/3/tutorial/introduction.html#lists
        # we are splitting at the ,
        line_values = line.split(',')

        # print the list so you can see all of the values between the [] which symbolizes that it's a list
        print(line_values)

        # grabbing the value at [0] is called indexing.  we get the item in the list at index 1, which is the second item
        # all programming languages start counting at 0
        # the append is adding an item to the out_line list
        out_line.append(line_values[0])

        # print just to show that it's working
        print('we found size {}'.format(line_values[1]))

        # get the 'new' size from the
        new_size = convert_size(line_values[1])

        # append the new size to out line list
        out_line.append(new_size)

        # last just append our third value, at index 2
        out_line.append(line_values[2])

        print('we have created out_line list {}'.format(out_line))

        # add our line list to our larger out list so we can write it to a file later
        out.append(out_line)


## this right here is a much more simple way to loop over each line in the file.  The reason we don't use this
## is more technical that I need to explain, but basically it will break with large files and I don't want to set
## you up to fail.
# with open(path_to_csv, 'r') as csv_file:
#     for line in csv_file.readlines():
#         # do stuff with line

# just to show the gap between reading and writing
print('##################################')

# now we need to write out to a new file
# the 'w' is opening the file in write mode.  write only, no reading
with open(path_to_out_csv, 'w') as csv_file:
    for line in out:
        string_to_write = ','.join(line)
        print('writing string "{}" to file'.format(string_to_write))
        csv_file.write(string_to_write)
