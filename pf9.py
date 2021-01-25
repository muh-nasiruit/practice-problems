''' 9. Design a function that will help you to encrypt your message. 
    '''

def msg_crypt(code, size):
    msg = []
    m_crypt = []
    up_ch = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']
    low_ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    for i in code:
        if i in up_ch:
            index = up_ch.index(i)
            crypt = (index + size) % 26
            m_crypt.append(crypt)
            n_msg = up_ch[crypt]
            msg.append(n_msg)
        elif i in low_ch:
            index = low_ch.index(i)
            crypt = (index + size) % 26
            m_crypt.append(crypt)
            n_msg = low_ch[crypt]
            msg.append(n_msg)
    return msg
msg_crypt('ashar', 3)