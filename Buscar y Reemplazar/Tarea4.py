posiciones = []

NO_OF_CHARS = 256

def badCharHeuristic(string, size):
    badChar = [-1]*NO_OF_CHARS
    for i in range(size):
        badChar[ord(string[i])] = i;
    return badChar

def search(txt, pat,posiciones):
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat, m) 
    s = 0
    while(s <= n-m):
        j = m-1
        while j>=0 and pat[j] == txt[s+j]:
            j -= 1
        if j<0:
            print("Pattern occur at shift = {}".format(s))
            posiciones.append(s)
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
        else:
            s += max(1, j-badChar[ord(txt[s+j])])
    return posiciones        
             

txt = str("El vídeo proporciona una manera eficaz para ayudarle a demostrar el punto. Cuando haga clic en vídeo en línea, puede pegar el código para insertar del vídeo que desea agregar. También puede escribir una palabra clave para buscar en línea el vídeo que mejor se adapte a su documento.")
pat = str("vídeo")
cambio = str("pelicula")
search(txt,pat,posiciones)
print(txt.replace(pat,cambio,len(posiciones)))