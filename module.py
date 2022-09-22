# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:13:18 2022

@author: Everton Castro
"""

class CalcIpv4:
    def __init__(self, ip: str, mascara :str):
        self._ip = ip
        self._mascara = mascara
        self.rede = ''
        self.mascara = ''
        self.broadcast = ''
        self.nIps = ''
        self.PrimeiroIp = ''
        self.UltimoIp = ''
        self.binario = []
        self.Separador_temp = []
        self.Separador()
        self.MascaraandBroadcast()
        
        for l in self.Separador_temp[:3]:
            self.rede += l + '.'
        self.broadcast = self.rede + self.broadcast + self._mascara
        self.PrimeiroIp = self.rede + '1' + self._mascara
        self.UltimoIp = self.rede + str(self.nIps) + self._mascara
        self.rede += '0' + self._mascara
        
        
    
    def Separador(self):
        ltemp = ''
        lcontador = 0
        for l in self._ip:
            if l == '.':
                self.Separador_temp.append(ltemp)
                self.Binario(int(ltemp))
                ltemp = ''

            else:
                ltemp += l
            lcontador += 1
            if lcontador == len(self._ip):
                self.Separador_temp.append(ltemp)
                self.Binario(int(ltemp))
                ltemp = ''
        
            
    def Binario(self, valor):
        if valor != None:
            valor_temp = format(valor,"b")
            while len(valor_temp) < 8:
                valor_temp = '0' + valor_temp
            self.binario.append(valor_temp)
            
    def binaryToDecimal(self, binary): 
        binary1 = binary 
        decimal, i, n = 0, 0, 0
        while(binary != 0): 
            dec = binary % 10
            decimal = decimal + dec * pow(2, i) 
            binary = binary//10
            i += 1
        return decimal
    
    def MascaraandBroadcast(self, ):
        ultimo_octeto = ''
        byte = len(self.Separador_temp) * 8    
        byte_temp = byte - int(self._mascara.replace('/', ''))
        if byte_temp < 8 :
            for i in range(byte_temp):
                ultimo_octeto += '0'
            broadcast_temp = ultimo_octeto
            broadcast_temp = broadcast_temp.replace('0', '1')
            self.broadcast = str(self.binaryToDecimal(int(broadcast_temp)))
            while len(ultimo_octeto) < 8:
                ultimo_octeto = '1' + ultimo_octeto
            
            
        self.nIps = 2 ** byte_temp - 2
        self.mascara = '255.255.255.' + str(self.binaryToDecimal(int(ultimo_octeto)))

        
        
    def Detalha(self):
        return f'IP E MÁSCARA PASSADOS: {self._ip}{self._mascara}, \
    \nMÁSCARA: {self.mascara}, \
    \nRede: {self.rede} \
        \nBroadcast: {self.broadcast},\nNºIps: {self.nIps} \
        \nPrimeiro Ip da rede: {self.PrimeiroIp}, \
        \nUltimo Ip da rede: {self.UltimoIp}'
    
                
if __name__ == '__main__':
    CalcIpv4('10.20.12.45')
    