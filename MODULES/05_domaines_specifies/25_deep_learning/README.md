# Chapitre 25 : Deep Learning avec PyTorch

## Introduction : Qu'est-ce que le Deep Learning ?

Le **Deep Learning** est une branche du Machine Learning basée sur les réseaux de neurones artificiels avec de nombreuses couches (d'où "deep"). Il excelle dans:
- Reconnaissance d'images
- Traitement du langage naturel
- Génération de texte/image/audio
- Jeux et robotique

---

## 1. Installation

```bash
uv sync --extra ai
```

**Note:** PyTorch avec CUDA peut prendre plusieurs Go. Sur CPU:
```python
import torch
print(f"PyTorch: {torch.__version__}")
print(f"CUDA disponible: {torch.cuda.is_available()}")
```

---

## 2. Tenseurs: Les Blocs de Base

```python
import torch

# Créer un tenseur
x = torch.tensor([1, 2, 3, 4])
print(x)  # tensor([1, 2, 3, 4])

# Tenseurs multidimensionnels
matrice = torch.tensor([[1, 2, 3],
                        [4, 5, 6]])
print(matrice.shape)  # torch.Size([2, 3])

# Tenseur aléatoire
x_alea = torch.rand(3, 3)  # 0 à 1

# Tenseur de zéros
zeros = torch.zeros(2, 2)

# Opérations
y = x + 5  # Addition scalaire
z = x * 2  # Multiplication scalaire

# Matrice multiplication
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])
resultat = torch.mm(a, b)
```

---

## 3. Autograd: Calcul Différentiel Automatique

```python
# Créer un tenseur avec gradient
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2  # y = x²

# Calculer le gradient
y.backward()

# dy/dx = 2*x = 4
print(x.grad)  # tensor(4.)

# Descente de gradient simple
x = torch.tensor(5.0, requires_grad=True)
for i in range(100):
    y = (x - 3) ** 2  # Fonction de perte
    y.backward()
    with torch.no_grad():
        x = x - 0.1 * x.grad  # Mise à jour
        x.grad.zero_()
print(f"x optimal: {x.item():.4f}")  #接近 3
```

---

## 4. Régression Linéaire avec PyTorch

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Données
X = torch.tensor([[1], [2], [3], [4], [5]], dtype=torch.float32)
y = torch.tensor([[100], [150], [200], [250], [300]], dtype=torch.float32)

# Modèle linéaire
model = nn.Linear(1, 1)  # 1 entrée, 1 sortie

# Fonction de perte et optimiseur
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Entraînement
for epoch in range(1000):
    predictions = model(X)
    loss = criterion(predictions, y)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 200 == 0:
        print(f'Epoch {epoch+1}, Loss: {loss.item():.4f}')

# Prédiction
nouveau_x = torch.tensor([[6.0]])
print(f'Prediction pour x=6: {model(nouveau_x).item():.2f}')
```

---

## 5. Réseau de Neurones Complet

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Définir le réseau
class reseau(nn.Module):
    def __init__(self):
        super().__init__()
        self.couche1 = nn.Linear(4, 8)   # 4 entrées -> 8 hidden
        self.couche2 = nn.Linear(8, 4)   # 8 -> 4 hidden
        self.couche3 = nn.Linear(4, 1)   # 4 -> 1 sortie
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        x = self.relu(self.couche1(x))
        x = self.relu(self.couche2(x))
        x = self.sigmoid(self.couche3(x))
        return x

model = reseau()
print(model)
```

---

## 6. Classification avec MNIST

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# Transformation des images
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Charger MNIST
train_data = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

# Réseau convolutif
class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)
        self.dropout = nn.Dropout(0.5)
    
    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 64 * 7 * 7)
        x = self.dropout(torch.relu(self.fc1(x)))
        x = self.fc2(x)
        return x

model = CNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Entraînement
for epoch in range(10):
    for images, labels in train_loader:
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    print(f'Epoch {epoch+1}, Loss: {loss.item():.4f}')
```

---

## 7. Transfer Learning

```python
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from torchvision import datasets
from torch.utils.data import DataLoader

# Utiliser un modèle pré-entraîné
model = models.resnet18(pretrained=True)

# Geler les couches
for param in model.parameters():
    param.requires_grad = False

# Remplacer la dernière couche
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 10)  # 10 classes

# Nouvel optimiseur
optimizer = optim.Adam(model.fc.parameters(), lr=0.001)

# Fine-tuning
for epoch in range(10):
    for images, labels in train_loader:
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
```

---

## 8. LSTM pour Séquences

```python
import torch
import torch.nn as nn

class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super().__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])  # Dernière sortie
        return out

# Exemple d'utilisation
model = LSTMModel(input_size=1, hidden_size=64, num_layers=2, output_size=1)
```

---

## 9. Sauvegarde et Chargement

```python
# Sauvegarder le modèle
torch.save({
    'epoch': 50,
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'loss': loss.item(),
}, 'mon_modele.pth')

# Charger le modèle
checkpoint = torch.load('mon_modele.pth')
model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
start_epoch = checkpoint['epoch'] + 1
```

---

## 10. GPU et Parallélisme

```python
# Vérifier GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Device: {device}")

# Envoyer le modèle sur GPU
model = model.to(device)

# Envoyer les données sur GPU
images = images.to(device)
labels = labels.to(device)

# DataParallel pour plusieurs GPU
if torch.cuda.device_count() > 1:
    model = nn.DataParallel(model)
```

---

## 11. Erreurs Courantes

### 1. Shape mismatch

```python
# MAUVAIS
x = torch.randn(10, 5)
y = torch.randn(10, 6)  # Différent!

# CORRECT - Vérifier les shapes
print(x.shape, y.shape)
```

### 2. Oublier zero_grad

```python
# MAUVAIS - Gradients accumulés
for data in loader:
    outputs = model(data)
    loss = criterion(outputs, labels)
    loss.backward()

# CORRECT - Remettre les gradients à zéro
optimizer.zero_grad()
for data in loader:
    outputs = model(data)
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()
```

### 3. Mode train/eval

```python
# Évaluation
model.eval()
with torch.no_grad():
    predictions = model(test_data)

# Retour au entraînement
model.train()
```

---

## 12. Projet: Classification d'Images

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Utilisation de: {device}")

# Données
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

train_data = datasets.ImageFolder('train/', transform=transform)
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)

# Modèle (simplifié VGG)
class SimpleVGG(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(64, 128, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.classifier = nn.Linear(128 * 56 * 56, num_classes)
    
    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x

model = SimpleVGG(num_classes=10).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Entraînement
for epoch in range(10):
    model.train()
    total_loss = 0
    correct = 0
    total = 0
    
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    
    print(f'Epoch {epoch+1}: Loss={total_loss/len(train_loader):.4f}, Accuracy={100*correct/total:.2f}%')
```

---

## Résumé PyTorch

| Concept | Description |
|---------|-------------|
| **Tensor** | Tableau multidimensionnel |
| **nn.Module** | Classe de base pour les modèles |
| **forward()** | Passage avant (prédiction) |
| **backward()** | Calcul des gradients |
| **DataLoader** | Gestion des batches |
| **transforms** | Prétraitement des images |
| **torchvision** | Modèles et datasets pré-entraînés |

---

## Pour Aller Plus Loin

- **NLP:** Hugging Face Transformers
- **Vision:** Detectron2, YOLO
- **Gan:** StyleGAN, DCGAN
- **RL:** Stable Baselines3

---

## Prochaines Étapes

Tu as complété le parcours Python Mastery ! Pour continuer:
1. Projet personnel intégrant plusieurs compétences
2. Contribuer à des projets open source
3. Certifications (TensorFlow, AWS ML)

---

*Félicitations ! Tu es maintenant prêt pour le Deep Learning! 🧠*
