import ezgmail
import os,sys

def searchBySender(senderToSearch):
    print(f'Searching for emails from {senderToSearch}...')
    searchedEmails = ezgmail.search(maxResults=500, query=f'from:{senderToSearch}' )
    return searchedEmails

def deleteEmails(emailsToDelete):
    print(f'Deleting {len(emailsToDelete)} emails...')
    for email in emailsToDelete:
        email.trash()

def deleteByUsers(fileToRead):
    ezgmail.init()
    f = open(fileToRead)
    sendersToDelete = f.readlines()
    f.close()
    for line in sendersToDelete:
        if line in ['','\n']:
            raise ValueError('Empty line error.')
        if len(line) < 5:
            userInput = 'nopenotyet'
            while userInput != 'y':
                userInput = input(f'Short input: {line}. Enter \'y\' to proceed.')
                if userInput == 'y':
                    break
        senderToDelete = line.strip()
        searchedEmails = searchBySender(senderToDelete)
        while len(searchedEmails) > 0:
            deleteEmails(searchedEmails)
            searchedEmails = searchBySender(senderToDelete)


if __name__ == '__main__':
    fileToRead = sys.argv[1]
    deleteByUsers(fileToRead)