# -*- coding: utf-8 -*-
"""
[암호분석 - 고전암호 구현] - Caeser 암호를 만들기 위한 Python 기초
- 입력함수: input()

- 문자열 다루기: 추출, 병합, Slicing(:)
- 부분 문자열 검색: find()
- 문자열 길이: len()

- 연산자: %
- 함수 정의하기
- for 반복문
"""

#==(1)== 문자열 다루기 (1)
print('Hello,' + ' Python.')

str1 = 'Hello, Cryptanalysis'
print(str1[-10:])   # Slicing 


print('What is your name?')
my_name = input()
print('Nice to meet you, ' + my_name + '.')
print('The length of your name =', len(my_name))

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet.find('ijk'))


#==(2)=== 문자열 다루기 (2)
upAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowAlphabet = 'abcdefghijklmnopqrstuvwxyz'

idx = upAlphabet.find('Z')
cipher = upAlphabet[(idx + 3) % 26]
print(cipher)


#==(3)=== 시저암호 구현
plaintext_msg = 'This is a plaintext message.'
key = 3

ciphertext_msg = ''
for ch in plaintext_msg:
    if ch in upAlphabet:
        idx = upAlphabet.find(ch)
        new_idx = (idx + key) % 26
        cipher_ch = upAlphabet[new_idx]
        ciphertext_msg = ciphertext_msg + cipher_ch    
    elif ch in lowAlphabet:
        idx = lowAlphabet.find(ch)
        new_idx = (idx + key) % 26
        cipher_ch = lowAlphabet[new_idx]
        ciphertext_msg = ciphertext_msg + cipher_ch
    else:
        ciphertext_msg = ciphertext_msg + ch


print('Plaintext  = ', plaintext_msg)
print('Ciphertext = ', ciphertext_msg)


#==(4)== 함수로 구현된 시저암호
def caesar_encrypt(msg, key):
    upAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowAlphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext_msg = ''
    for ch in msg:
        if ch in upAlphabet:
            idx = upAlphabet.find(ch)
            new_idx = (idx + key) % 26
            cipher_ch = upAlphabet[new_idx]
            ciphertext_msg = ciphertext_msg + cipher_ch    
        elif ch in lowAlphabet:
            idx = lowAlphabet.find(ch)
            new_idx = (idx + key) % 26
            cipher_ch = lowAlphabet[new_idx]
            ciphertext_msg = ciphertext_msg + cipher_ch
        else:
            ciphertext_msg = ciphertext_msg + ch    
    return ciphertext_msg

def caesar_decrypt(msg, key):
    upAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowAlphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext_msg = ''
    for ch in msg:
        if ch in upAlphabet:
            idx = upAlphabet.find(ch)
            new_idx = (idx - key) % 26
            cipher_ch = upAlphabet[new_idx]
            ciphertext_msg = ciphertext_msg + cipher_ch    
        elif ch in lowAlphabet:
            idx = lowAlphabet.find(ch)
            new_idx = (idx - key) % 26
            cipher_ch = lowAlphabet[new_idx]
            ciphertext_msg = ciphertext_msg + cipher_ch
        else:
            ciphertext_msg = ciphertext_msg + ch    
    return ciphertext_msg

#----- 함수 활용

plaintext_msg = 'This is a plaintext message.'
key = 3

ciphertext = caesar_encrypt(plaintext_msg, key)

print('Plaintext  = ', plaintext_msg)
print('Ciphertext = ', ciphertext)

recovered_msg = caesar_decrypt(ciphertext, key)

print('Ciphertext = ', ciphertext)
print('Recovered text = ', recovered_msg)


#==(5)== 시저암호의 공격(해독)

for key_guess in range(0,26):
    recovered_guess = caesar_decrypt(ciphertext, key_guess)
    print('key =', key_guess, ' : ', recovered_guess)
    
'''    
#== 실행결과
key = 0  :  Wklv lv d sodlqwhaw phvvdjh.
key = 1  :  Vjku ku c rnckpvgzv oguucig.
key = 2  :  Uijt jt b qmbjoufyu nfttbhf.
key = 3  :  This is a plaintext message.
key = 4  :  Sghr hr z okzhmsdws ldrrzfd.
key = 5  :  Rfgq gq y njyglrcvr kcqqyec.
key = 6  :  Qefp fp x mixfkqbuq jbppxdb.
key = 7  :  Pdeo eo w lhwejpatp iaoowca.
key = 8  :  Ocdn dn v kgvdiozso hznnvbz.
key = 9  :  Nbcm cm u jfuchnyrn gymmuay.
key = 10  :  Mabl bl t ietbgmxqm fxlltzx.
key = 11  :  Lzak ak s hdsaflwpl ewkksyw.
key = 12  :  Kyzj zj r gcrzekvok dvjjrxv.
key = 13  :  Jxyi yi q fbqydjunj cuiiqwu.
key = 14  :  Iwxh xh p eapxcitmi bthhpvt.
key = 15  :  Hvwg wg o dzowbhslh asggous.
key = 16  :  Guvf vf n cynvagrkg zrffntr.
key = 17  :  Ftue ue m bxmuzfqjf yqeemsq.
key = 18  :  Estd td l awltyepie xpddlrp.
key = 19  :  Drsc sc k zvksxdohd wocckqo.
key = 20  :  Cqrb rb j yujrwcngc vnbbjpn.
key = 21  :  Bpqa qa i xtiqvbmfb umaaiom.
key = 22  :  Aopz pz h wshpualea tlzzhnl.
key = 23  :  Znoy oy g vrgotzkdz skyygmk.
key = 24  :  Ymnx nx f uqfnsyjcy rjxxflj.
key = 25  :  Xlmw mw e tpemrxibx qiwweki.    
'''





