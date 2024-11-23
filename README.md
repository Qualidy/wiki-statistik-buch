**Repository klonen:**

```commandline
git clone https://github.com/Qualidy/wiki-statistik-buch.git
```

**Virtuelle Umgebung anlegen:**

Auf Windows:

```commandline
python -m venv .venv
```

Auf Mac:

```commandline
python3 -m venv .venv
```

**Virtuelle Umgebung aktivieren:**

Auf Windows:

```commandline
.\.venv\Scripts\Activate.ps1
```

Auf Mac:

```commandline
source .venv/bin/activate
```

**Abhängigkeiten installieren:**

Auf Windows:

```commandline
pip install -r requirements.txt
```

Auf Mac:

```commandline
pip3 install -r requirements.txt
```

**Lokal Webseite ausführen:**

```commandline
mkdocs serve
```

**Webseite veröffentlichen:**

Es werden automatisch die Inhalte des `main`-Branches veröffentlicht.

Wenn die Veröffentlichung automatisch angestoßen werden soll, so kann das mit dem folgenden Befehl getan werden:

```commandline
mkdocs gh-deploy
```

**Webseite bearbeiten und veröffentlichen:**

1. Aktuelle Version holen
```commandline
git pull
```
2. Vorschau starten
Markdown-Dateien unter docs/content bearbeiten. 
Vorschau anzeigen mit:

```commandline
mkdocs serve
```

3. Änderungen speichern
- Status prüfen:

```commandline
git status
```

- Änderungen hinzufügen:

```commandline
git add .
```

- Commit erstellen:

```commandline
git commit -m "Beschreibung der Änderungen"
```

- Änderungen hochladen:

```commandline
git push
```
