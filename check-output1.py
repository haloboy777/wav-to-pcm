from pcm_channels import pcm_channels

m=[];
a = pcm_channels('output.wav');

print(len(a[0][0]));

for l in a[0][0]:
    if l<=l+5 and l>=l-5:
        m.append(1);
    else:
        m.append(0);

print(a[0][0]);